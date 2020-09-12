from pwn import *

r = remote("localhost", 9004)

with open("exploit.js", "r") as f:
    code = f.read()

r.recvline()
r.sendline(code)
r.shutdown('write')

r.interactive()

# FLAG --> ASIS{w1ld_3xpl01t_3sc4p3d_fr0m_s4f4r1_m1t1g4t10n}

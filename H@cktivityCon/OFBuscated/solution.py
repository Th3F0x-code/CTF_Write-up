from Crypto.Util.Padding import pad
from pwn import *

crib = pad('}', 16)
r = connect("jh2i.com", 50028)
c = r.recvuntil('\n')[:-1]
# print(c,len(c))
c = c.decode('hex')
xored = xor(crib, c)
for i in range(10):
    r = connect("jh2i.com", 50028)
    c = r.recvuntil('\n')[:-1]
    c = c.decode('hex')
    print(xor(xored, c))

# FLAG --> flag{bop_it_twist_it_pull_it_lol}

from Crypto.Util.Padding import pad
from pwn import *

HOST = "jh2i.com"
PORT = 50028
r = connect(HOST, PORT)

crib = pad(b'}', 16)
c = r.recvuntil('\n')[:-1]
# print(c,len(c))
c = c.decode('hex')
xored = xor(crib, c)
for i in range(10):
    r = connect(HOST, PORT)
    c = r.recvuntil('\n')[:-1]
    c = c.decode('hex')
    print(xor(xored, c))

# FLAG --> flag{bop_it_twist_it_pull_it_lol}

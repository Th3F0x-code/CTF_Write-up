import os

os.environ["PWNLIB_NOTERM"] = "True"

from pwn import *

IP = "76.74.178.201"
PORT = 9531
r = remote(IP, PORT, level="debug")
POW = r.recvline().decode().split()
x_len = int(POW[-1])
suffix = POW[-5]
hash_type = POW[-7].split('(')[0]

"""
The server asks for a random length string, hashed with a random hash
function such that the last 3 bytes of the hash match a given prefix.
"""
while True:
    X = ''.join(random.choices(string.ascii_letters + string.digits, k=x_len))
    h = getattr(hashlib, hash_type)(X.encode()).hexdigest()
    if h.endswith(suffix):
        print(h)
        break

r.sendline(X)

header = r.recvuntil(b'One of such points')

points = r.recvline().split(b'P = (')[-1]
points = points.split(b', ')
px = Integer(points[0])
py = Integer(points[-1][:-2])

scale_data = r.recvline().split(b' ')
scale = Integer(scale_data[3])

p = px + 1
assert p.is_prime()
a = -1
b = (py ^ 2 - px ^ 3 - a * px) % p
E = EllipticCurve(GF(p), [a, b])
P = E(px, py)

Q = P * scale

"""
For some reason sending str(Q.xy()) to the server caused an error, so I 
just switched to interactive and sent it myself. I'm sure it's a dumb
formatting bug, but with the annoying POW to deal with, I can't be bothered
to figure it out...
"""
# r.sendline(str(Q.xy()))
print(Q.xy())
r.interactive()

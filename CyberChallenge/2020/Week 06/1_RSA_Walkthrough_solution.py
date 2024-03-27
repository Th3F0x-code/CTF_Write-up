from binascii import *

from Crypto.Util.number import inverse
from pwn import *

HOST = "rsa.challs.cyberchallenge.it"
PORT = 9040
r = remote(HOST, PORT)

# Level 1
r.recvuntil('p = ')
p = int(r.recvline().decode()[0:-1])
r.recvuntil('q = ')
q = int(r.recvline().decode()[0:-1])

n = p * q
r.sendline(str(n).encode())

# Level 2
r.recvuntil('message = ')
message = r.recvline().decode()[0:-1]

h = hexlify(message.encode())
m = int(h, 16)
r.sendline(str(m).encode())

# Level 3
r.recvuntil('p = ')
p = int(r.recvline().decode()[0:-1])
r.recvuntil('q = ')
q = int(r.recvline().decode()[0:-1])
r.recvuntil('m = ')
m = int(r.recvline().decode()[0:-1])
r.recvuntil('e = ')
e = int(r.recvline().decode()[0:-1])

n = p * q
c = pow(m, e, n)
r.sendline(str(c).encode())

# Level 4
r.recvuntil('p = ')
p = int(r.recvline().decode()[0:-1])
r.recvuntil('q = ')
q = int(r.recvline().decode()[0:-1])
r.recvuntil('e = ')
e = int(r.recvline().decode()[0:-1])

phi = (p - 1) * (q - 1)
r.sendline(str(phi).encode())

d = inverse(e, phi)
r.sendline(str(d).encode())

# Level 5
r.recvuntil('p = ')
p = int(r.recvline().decode()[0:-1])
r.recvuntil('q = ')
q = int(r.recvline().decode()[0:-1])
r.recvuntil('e = ')
e = int(r.recvline().decode()[0:-1])
r.recvuntil('c = ')
c = int(r.recvline().decode()[0:-1])

n = p * q
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)
r.sendline(str(m).encode())

r.recvline()[0:-1]
r.recvline()[0:-1]
print(r.recvline().decode()[0:-1])
print(r.recvline().decode()[0:-1])

# FLAG --> CCIT{W3lc0me_t0_RSA!}

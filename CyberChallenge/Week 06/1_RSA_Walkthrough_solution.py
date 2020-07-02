from binascii import hexlify

from pwn import *


def level_1(p, q):
    n = p * q
    return str(n)


def level_2(msg):
    m = int(hexlify(msg.encode("ascii")), 16)
    return str(m)


def level_3(p, q, m, e):
    n = p * q
    c = pow(m, e, n)
    return str(c)


def level_4(p, q):
    tot = (p - 1) * (q - 1)
    return str(tot)


def level_4_2(e, tot):
    d = pow(e, -1, tot)
    return str(d)


def level_5(c, d, n):
    m = pow(c, d, n)
    return str(m)


HOST = "rsa.challs.cyberchallenge.it"
PORT = 7010
p = remote(HOST, PORT)

p.recvuntil("p = ")
x = int(p.recvline().strip())
print("p = " + str(x))
p.recvuntil("q = ")
y = int(p.recvline().strip())
print("q = " + str(y))
p.sendlineafter("n = ?\n", level_1(x, y))
print("n = " + level_1(x, y))

print(p.recvline().strip())
print(p.recvline().strip())

p.recvuntil("message = ")
t = p.recvline().strip()
print("m = %d " % int(level_2(t.decode("ascii"))))
p.sendlineafter("m = ?\n", level_2(t.decode("ascii")))

print(p.recvline().strip())
print(p.recvline().strip())

p.recvuntil("p = ")
b = int(p.recvline().strip())
print("p = %d" % b)

p.recvuntil("q = ")
c = int(p.recvline().strip())
print("q = %d" % c)

p.recvuntil("m = ")
m = int(p.recvline().strip())
print("m = %d" % m)

p.recvuntil("e = ")
e = int(p.recvline().strip())
print("e = %d" % e)

print("c = %d" % int(level_3(b, c, m, e)))
p.sendlineafter("c = ?\n", level_3(b, c, m, e))
print(p.recvline().strip())
print(p.recvline().strip())

p.recvuntil("p = ")
v = int(p.recvline().strip())
print("p = %d" % v)

p.recvuntil("q = ")
w = int(p.recvline().strip())
print("q = %d" % w)

p.recvuntil("e = ")
y = int(p.recvline().strip())
print("e = %d" % y)

print("tot(n) = %d" % int(level_4(v, w)))
p.sendlineafter("tot(n) = ?\n", level_4(v, w))

print(p.recvline().strip())

print("d = %d" % int(level_4_2(y, int(level_4(v, w)))))
p.sendlineafter("d = ?\n", level_4_2(y, int(level_4(v, w))))
print(p.recvline().strip())
print(p.recvline().strip())

p.recvuntil("p = ")
z = int(p.recvline().strip())
print("p = %d" % z)

p.recvuntil("q = ")
k = int(p.recvline().strip())
print("q = %d" % k)

p.recvuntil("e = ")
i = int(p.recvline().strip())
print("e = %d" % i)

p.recvuntil("c = ")
o = int(p.recvline().strip())
print("c = %d" % o)

print("m = %d" % int(level_5(o, int(level_4_2(i, int(level_4(z, k)))), int(level_1(z, k)))))
p.sendlineafter("m = ?\n", level_5(o, int(level_4_2(i, int(level_4(z, k)))), int(level_1(z, k))))
p.recvuntil("Great! Here's your flag:\n")
print("flag: " + p.recvline().decode())

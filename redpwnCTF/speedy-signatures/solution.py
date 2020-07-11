import itertools

import ecdsa
import gmpy2
from ecdsa.ecdsa import Public_key, Signature
from ecdsa.ellipticcurve import Point
from pwn import *
from tqdm import tqdm


def legendre(a, p):
    return pow(a, (p - 1) // 2, p)


def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


C = ecdsa.NIST256p
G = C.generator
p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
a = -3
b = 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B
n = C.order


def point(x):
    y = tonelli(((pow(x, 2) + a) * x + b) % p, p)
    return Point(C.curve, x, y), Point(C.curve, x, -y)


def inv(x):
    return gmpy2.invert(x, n)


m1 = b'a'
m2 = b'b'
h1 = int(hashlib.sha256(m1).hexdigest(), 16)
h2 = int(hashlib.sha256(m2).hexdigest(), 16)

HOST = "2020.redpwnc.tf"
PORT = 31452
nc = remote(HOST, PORT)


def recv():
    nc.recvline()
    Q = Public_key(G, Point(C.curve, *map(int, nc.recvline().split(b' '))))
    nc.sendlineafter(': ', m1)
    nc.sendlineafter(': ', m2)
    return Q, list(map(int, nc.recvline().split(b' ')))


def send(x):
    nc.recvline()
    nc.sendline(str(x))
    assert b'Correct' in nc.recvline()
    out = nc.recvline()
    if b'flag' in out:
        print(out)


Q, vals = recv()
for r1, s1, s2 in itertools.permutations(vals):
    if Q.verifies(h1, Signature(r1, s1)):
        swap = False
        break
    elif Q.verifies(h2, Signature(r1, s1)):
        t = m1;
        m1 = m2;
        m2 = t
        t = h1;
        h1 = h2;
        h2 = t
        swap = True
        break
else:
    print('none')
    sys.exit()

possible = point(r1)
for diff in tqdm(range(-4095, 4095)):
    for H1 in possible:
        H2 = H1 + diff * G
        r2 = H2.x()
        if Q.verifies(h2, Signature(r2, s2)):
            break
    else:
        continue
    break
else:
    print('error finding other r2')
    sys.exit()

if swap:
    diff = -diff
d = (diff + inv(s1) * h1 - inv(s2) * h2) * inv(inv(s2) * r2 - inv(s1) * r1) % n
assert d * G == Q.point
send(d)
k = inv(s1) * (h1 + r1 * d) % n


def guess():
    Q, vals = recv()
    for s1 in vals:
        for diff in range(-4095, 4096):
            k1 = k + diff
            H1 = k1 * G
            r1 = H1.x()
            d = (s1 * k1 - h1) * inv(r1) % n
            if d * G == Q.point:
                send(d)
                return
            d = (s1 * k1 - h2) * inv(r1) % n
            if d * G == Q.point:
                send(d)
                return
    print('no guess found')
    sys.exit()


for i in tqdm(range(99)):
    guess()

nc.interactive()

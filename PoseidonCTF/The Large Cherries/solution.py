from pwn import *
from z3.z3 import Solver, BitVec

host = "localhost"
port = 3001
p = remote(host, port)
a = [BitVec('a%s' % i, 64) for i in range(9)]

s = Solver()
s.add(a[3] + a[0] == 0xab)
s.add(a[3] == 0x37)
s.add(a[2] ^ a[1] == 0x5d)
s.add(a[4] - a[2] == 5)
s.add(a[6] + a[4] == 0xa2)
s.add(a[5] == a[6])
s.add(a[6] == 0x30)
s.add(a[7] == 0x7a)
s.check()
m = s.model()
print(s.model())
b = []
for i in range(8):
    b.append(chr(int(m[a[i]].as_string())))
c = ''.join(b)
print(c)
p.sendlineafter("Enter the secret for the magic word: ", c)
p.stream()

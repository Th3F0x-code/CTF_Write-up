from z3 import *

s = Solver()


def mul(a, b):
    aa = ZeroExt(32, a)
    bb = ZeroExt(32, b)
    return aa * bb


def mul3(a, b, c):
    aa = ZeroExt(32, a)
    bb = ZeroExt(32, b)
    cc = ZeroExt(32, c)
    return aa * bb * cc


sz = 34
p = [BitVec('p%d' % i, 8) for i in range(sz)]
u = [BitVec('u%d' % i, 8) for i in range(6)]

s.add(mul(p[0], p[sz // 2 - 1]) == 0x1d93)  # 0000f747
s.add(u[2] == p[sz // 2 - 1] + 4)  # 0000f79b
s.add(mul(p[0], p[sz // 2 - 2]) == 0x174b)  # 0000f7d7
s.add(p[sz // 2 + sz // 2 - 1] == u[0])  # 0000f7e9
s.add(mul(p[sz // 2 - 2], p[2]) == 0x21b9)  # 0000f813
s.add(u[4] == p[2] + 4)  # 0000f848
s.add(mul3(p[2], p[1], p[sz // 2 - 3]) == 0xca745)  # 0000f896
s.add(p[sz // 2 + 2] == u[3])  # 0000f8a5
s.add(mul3(p[sz // 2 - 4] - 0x20, p[3], p[4]) == 0x7c4d5)  # 0000f90c
s.add(p[4] == u[1])  # 0000f91d
s.add(mul3(p[sz // 2 - 5], p[5], p[sz // 2 - 6]) == 0x96a6d)  # 0000f980
s.add(mul3(p[6], p[sz // 2 - 6], p[sz // 2 - 7]) == 0xed8f3)  # 0000f9c7
s.add(u[5] == p[sz // 2 + 6])  # 0000f9d6
s.add(mul(p[7], p[3]) == 0xeb3)  # 0000f9ff
s.add(mul(p[sz // 2 - 8], p[5]) == 0x10d3)  # 0000fa30
s.add(mul(p[sz // 2 - 9], p[sz // 2 - 4]) == 0x3116)  # 0000fa61

for i in range(sz // 2):
    s.add(p[sz // 2 + i] == p[i] + 1)

s.check()
m = s.model()

password = ''.join([chr(m[p[x]].as_long()) for x in range(sz)])
user = ''.join([chr(m[u[x]].as_long()) for x in range(6)])

print("Username --> " + user)
print("Password --> " + password)
# FLAG --> ASIS{F0r_ev3ry_0ne_th4t_a5ke7h_r3ceive7h_4nd_h3_th4t_s33ke7h_f1nde7h_4nd_t0_h1m_th4t_kn0cke7h_1t_5hall_8e_0pen3d}

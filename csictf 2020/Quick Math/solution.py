from gmpy2 import iroot
from sympy.ntheory.modular import crt

n = [86812553978993, 81744303091421, 83695120256591]
c = [8875674977048, 70744354709710, 29146719498409]

e = 3

resultant, mod = crt(n, c)
value, is_perfect = iroot(resultant, e)
if is_perfect:
    asd = value
print("csictf{" + bytearray.fromhex("683435743464").decode() + "}")

c = 32949
n = 64741
e = 42667
p = 101
q = 641

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

m = pow(c, d, n)
print(m)
flag = long_to_bytes(m).decode()
print(flag)

import mod

c = 32949
n = 64741
e = 42667

p = None
for i in range(2, n):
    if n % i == 0:
        p = i
        break

q = n // p
em = mod.Mod(e, (p - 1) * (q - 1))
d = int(1 // em)
cm = mod.Mod(c, n)
ans = int(cm ** d)
print(ans)

# FLAG --> csictf{gr34t_m1nds_th1nk_4l1ke}

import string

a = [20,77,94,76,74,78,29,81,86,92,76,95,132,79,95,81,101,111,98,98,86,106,88,143,90,106,92,112,122,112,108,105,98,153,99,118,116,43,128]

for i in range(len(a)):
    a[i] -= i

for x in range(256):
    b = list(a)
    for i in range(len(b)):
        b[i] ^= x
    if all(chr(x) in string.printable[:-5] for x in b):
        print(''.join(map(chr, b)))

# FLAG --> 3k{nan0mites_everywhere_everytime_ftw!}

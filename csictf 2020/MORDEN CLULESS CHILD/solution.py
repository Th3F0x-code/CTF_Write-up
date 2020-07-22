cipher = "52f41f58f51f47f57f49f48f5df46f6ef53f43f57f6cf50f6df53f53f40f58f51f6ef42f56f43f41f5ef5cf4e".split('f')
key = ['3' + i for i in "12123"]

res = []
for i, n in enumerate(cipher):
    x = int(n, 16)
    y = int(key[i % len(key)], 16)
    res.append(hex(x ^ y)[2:])

res = "".join(res)
print(bytes.fromhex(res).decode())

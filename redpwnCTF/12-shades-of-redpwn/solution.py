f = open("cipher.txt", "r")

for line in f:
    x, y = line.split()
    x, y = int(x), int(y)
    print(chr(x * 12 + y), end="")
print()

# FLAG --> flag{9u3ss1n9_1s_4n_4rt}

cts = open('./output.txt').read().splitlines()
Z = zip(*cts)


def least_freq(lst):
    return '1' if lst.count('0') > lst.count('1') else '0'


flag = ''.join(least_freq(B) for B in Z)
print(bytes.fromhex(hex(int(flag, 2))[2:]).decode())

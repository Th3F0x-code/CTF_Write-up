#!/usr/bin/env python2.7

import sys
from binascii import hexlify, unhexlify
from string import printable
from Crypto.Cipher import AES


def xor(s1, s2):
    return [a ^ b for a, b in zip(s1, s2)]


def xor_char(s1, s2):
    return [chr(a ^ b) for a, b in zip(s1, s2)]


def from_hexstring_to_array_of_int(hexstring):
    arr = []
    for i in range(0, len(hexstring), 2):
        arr.append(int(hexstring[i:(i + 2)], 16))
    return arr


# KEY = "yn9RB3Lr43xJK2██".encode()
# IV  = "████████████████".encode() #16 characters
KEY = "yn9RB3Lr43xJK2aa".encode()
IV = "aaaaaaaaaaaaaaaa".encode()  # 16 characters
msg = "AES with CBC is very unbreakable".encode()  # 32 characters

aes = AES.new(KEY, AES.MODE_CBC, IV)
result = aes.encrypt(msg)
pretty_result = hexlify(result).decode()
# print(pretty_result)

c0 = result[:16]
c1 = result[16:]
new_aes = AES.new(KEY)
dec = hexlify(new_aes.decrypt(c1)).decode()

# output:
# c5██████████████████████████d49e78c670cb67a9e5773d696dc96b78c4e0
# 26 blocks obscured + 38 clear = 64


# %%
initial_key = 'yn9RB3Lr43xJK2'
b1 = '78c670cb67a9e5773d696dc96b78c4e0'

for c1 in printable[:-6]:
    for c2 in printable[:-6]:
        new_key = initial_key + c1 + c2
        alg = AES.new(new_key.encode())
        p1_xor_b0 = alg.decrypt(bytes.fromhex(b1))
        dec_array = from_hexstring_to_array_of_int(hexlify(p1_xor_b0).decode())
        b0_0 = ord('v') ^ 197
        b0_14 = ord('l') ^ 212
        b0_15 = ord('e') ^ 158
        if (dec_array[0] == b0_0) and (dec_array[14] == b0_14) and (dec_array[15] == b0_15):
            print(new_key)
            print(hexlify(p1_xor_b0).decode())
            break

# %%
FINAL_KEY = 'yn9RB3Lr43xJK2tp'
P1_XOR_C0 = 'b3b92bf320938d7000d9d3863148b8fb'
B0 = 'c5dc598a00e6e31272bcb2ed502ad49e'
flag = ""
another_alg = AES.new(FINAL_KEY.encode())
p0_xor_iv = another_alg.decrypt(bytes.fromhex(B0))
iv = xor(p0_xor_iv, msg[:16])
for el in iv:
    flag += chr(el)
print("Flag: CCIT{" + flag + "}")

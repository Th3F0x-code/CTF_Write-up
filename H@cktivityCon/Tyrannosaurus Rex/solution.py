from pwn import xor

s = "37151032694744553d12220a0f584315517477520e2b3c226b5b1e150f5549120e5540230202360f0d20220a376c0067".decode('hex')
crib = "Z"
flag = "Z"
for i in range(len(s)):
    flag += xor(s[i], flag[i])
print(flag[:-1].decode("base64"))

# FLAG --> flag{tyrannosauras_xor_in_reverse}

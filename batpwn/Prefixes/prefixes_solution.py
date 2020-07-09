ct = "eae4a5b1aad7964ec9f1f0bff0229cf1a11b22b11bfefecc9922aaf4bff0dd3c88"
ct = bytes.fromhex(ct)
flag = ""

initialize = 0
for i in range(len(ct)):
    for val in range(256):
        if (initialize ^ (val << 2) ^ val) & 0xff == ct[i]:
            flag += chr(val)  # the value val is found
            initialize ^= (val << 2) ^ val  # to get the value of initialize for nex iteration of i
            initialize >>= 8  # initialize is [0-3] since (val<<2)^(val) is 10 bits, which is right shifted 8 bits each iteration
            break
print(flag)

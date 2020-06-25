from pwn import *
import binascii
import hashlib

host = args.HOST or 'challs.m0lecon.it'
port = int(args.PORT or 11000)

io = connect(host, port)
secret = [-1 for i in range(128)]

def apply_secret(c):
    r = bin(c)[2:].rjust(128,'0')
    return int(''.join([str(r[i]) for i in secret]), 2)

def decrypt(s):  
    to_decrypt = int(s, 16)
    for ll in range(9):
        x = apply_secret((to_decrypt >> (640-128)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)
        reappear = ((to_decrypt >> 640) ^ x) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        to_decrypt = to_decrypt << 128 | reappear
        to_decrypt = to_decrypt % 2**(128*6)
    return hex(to_decrypt)[2:]

def solve(chall):
    io.recvuntil("2. Give me the decrypted challenge")
    io.sendline("2")
    ris = decrypt(chall)
    ris = binascii.unhexlify(ris)
    io.sendline(ris)
    return io.recvuntil("\n")

def pad32(s):
    m = 32 - len(s)
    return "0"*m + s

def send_enc(val):
    io.recvuntil("2. Give me the decrypted challenge")
    io.sendline("1")
    io.recvuntil("Give me something to encrypt (hex):\n")
    io.sendline(val)
    return io.recvuntil("\n")

def attempt(e):
    val = [pad32(hex(es)[2:]) for es in e]
    vals = int(send_enc("".join(val)),16)
    
    ret = []

    for i in range(6):
        ret.append(vals & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)
        vals = vals >> 128
    return ret

#PoW
io.recvuntil("sha256sum ends in ")
check = io.recvuntil(".",drop=True)
chk = ""
for i in range(1000000000000):
    if hashlib.sha256(str(i).encode('ascii')).hexdigest()[-6:] == check:
        print(hashlib.sha256(str(i).encode('ascii')).hexdigest()[-6:])
        print(check)
        chk = str(i)
        break
print(chk)

io.sendline(chk)

#start challlenge
print(io.recvuntil("Encrypted challenge (hex):\n"))
chall = io.recvuntil("\n")

#obtaining the secret permutation matrix
for req in range(128):
    if req in secret:
        continue
    val = 2**(127-req)
    vals = attempt([0,0,0,val,0,0])

    old = req
    #removing e2 from c5 = p**6 * e2 + e2
    vals[5] = vals[5]^val
    #compute the 6 permutations
    for i in range(6):
        pos = 128-len(bin(vals[i])[2:])
        secret[pos] = old
        old = pos

#decrypt and send
solve(chall)

io.interactive()

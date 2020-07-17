from pwn import *

p = remote("padding.challs.cyberchallenge.it", 7000)


def split(msg, BLOCK=32):
    return [msg[i:i + BLOCK] for i in range(0, len(msg), BLOCK)]


def encrypt(msg):
    p.sendline(msg)
    p.recvuntil("password: ")
    return split(p.recvline().strip())


flag = ""
while "}" not in flag:
    for _ in printable[:-6]:
        msg = "A" * (31 - len(flag)) + flag + _ + "A" * (31 - len(flag))
        blocks = encrypt(msg)
        if blocks[1] == blocks[3]:
            flag = flag + _
            print(flag)
            break

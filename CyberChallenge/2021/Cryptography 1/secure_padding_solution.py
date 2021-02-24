import string

from pwn import *

p = remote("padding.challs.cyberchallenge.it", 9030)


def split(msg, BLOCK=32):
    return [msg[i:i + BLOCK] for i in range(0, len(msg), BLOCK)]


def encrypt(msg):
    p.sendline(msg)
    p.recvuntil("password: ")
    return split(p.recvline().strip())


flag = ""
while "}" not in flag:
    for _ in string.printable[:-6]:
        msg = "A" * (31 - len(flag)) + flag + _ + "A" * (31 - len(flag))
        blocks = encrypt(msg)
        if blocks[1] == blocks[3]:
            flag = flag + _
            break
print("Flag --> %s" % flag)

# FLAG --> CCIT{r3m3mb3r_th3_3cb_p3ngu1n?}

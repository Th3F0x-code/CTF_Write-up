from pwn import *

from time import sleep

r = remote("piecewise.challs.cyberchallenge.it", 9110)
flag = b""
a = []
while True:

    a = r.recvline().split()
    print(a)
    if b"empty" in a:
        r.send("\n")
        # r.recvuntil("Partial flag: ")
        print(r.recvline().strip())
        a = []

    elif b"32-bit" in a and b"little-endian" in a:
        with context.local(endian='little'):
            r.send(p32(int(a[5])))
            # r.recvuntil("Partial flag: ")
            print(r.recvline().strip())
            a = []

    elif b"64-bit" in a and b"little-endian" in a:
        with context.local(endian='little'):
            r.send(p64(int(a[5])))
            # r.recvuntil("Partial flag: ")
            print(r.recvline().strip())
            a = []

    elif b"32-bit" in a and b"big-endian" in a:
        with context.local(endian='big'):
            r.send(p32(int(a[5])))
            # r.recvuntil("Partial flag: ")
            print(r.recvline().strip())
            a = []

    elif b"64-bit" in a and b"big-endian" in a:
        with context.local(endian='big'):
            r.send(p64(int(a[5])))
            # r.recvuntil("Partial flag: ")
            print(r.recvline().strip())
            a = []
    sleep(0.5)

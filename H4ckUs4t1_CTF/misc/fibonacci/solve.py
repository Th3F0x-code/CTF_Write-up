from pwn import *

elf = ELF("./fibonacci")
log.log_level = "debug"
# r = elf.process()
r = remote("localhost", 7024)


def fib(n):
    seq = []
    a, b = 0, 1
    for i in range(n):
        c = a + b
        a, b = b, c
        seq.append(c)
    return seq


a = fib(100)
print(a)
for i in range(1, 100):
    r.sendlineafter(b"n: ", str(a[i]).encode())
    print(r.recvline())

r.interactive()

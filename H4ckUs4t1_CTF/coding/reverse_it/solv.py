from pwn import *

# elf = ELF('./target/release/alphabet')

r = process("./target/release/reverse_it")

r.recvuntil(b'Press enter to continue...\n')
r.sendline(b'')
for _ in range(1000):
    r.recvuntil(b"Input: ")
    strings = r.recvline().strip().decode()
    n, string = strings.split(" ")
    n = int(n)
    if n % 2 == 0:
        r.sendlineafter(b'Output: ', string.encode())
    else:
        r.sendlineafter(b'Output: ', string[::-1].encode())

r.interactive()

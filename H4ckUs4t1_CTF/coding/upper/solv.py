from pwn import *

r = process("./target/release/upper")

r.recvuntil(b'Press enter to continue...\n')
r.sendline(b'')
for _ in range(1000):
    r.recvuntil(b"Input: ")
    string = r.recvline().strip()
    sol = string.swapcase()
    r.sendlineafter(b'Output: ', sol)

r.interactive()

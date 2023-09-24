from pwn import *

# elf = ELF('./target/release/alphabet')

r = process("./target/release/alphabet")

letters = [chr(i) for i in range(97, 123)]
print(letters)

r.recvuntil(b'Press enter to continue...\n')
r.sendline(b'')
for _ in range(1000):
    r.recvuntil(b"Input: ")
    n = r.recvline().strip().decode()
    print(n)
    sol = letters[(int(n) - 1)].upper() * (int(n))
    print(sol)
    # r.sendlineafter("",sol.encode())
    # print(r.recvline())
    r.sendlineafter(b'Output: ', sol.encode())

r.interactive()

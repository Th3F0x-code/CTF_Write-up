from pwn import *

# elf = ELF('./target/release/alphabet')

r = process("./target/release/numbers")

r.recvuntil(b'Press enter to continue...\n')
r.sendline(b'')

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
           "20"]
for _ in range(1000):
    r.recvuntil(b"Input: ")
    n = r.recvline().strip().decode()

    result = ""
    for i in range(1, int(n) + 1):
        result += numbers[i]

    r.sendlineafter(b'Output: ', result.encode() * int(n))

r.interactive()

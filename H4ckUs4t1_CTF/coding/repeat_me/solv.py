from pwn import *

# elf = ELF('./target/release/alphabet')

r = process("./target/release/repeat_me")

r.recvuntil(b'Press enter to continue...\n')
r.sendline(b'')
for _ in range(1000):
    r.recvuntil(b"Input: ")
    strings = r.recvline().strip().decode()
    string_1, string_2 = strings.split(" ")
    print(string_1, string_2)
    r.sendlineafter(b'Output: ', string_1.encode() * len(string_2))

r.interactive()

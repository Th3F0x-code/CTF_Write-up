from pwn import *

r = process("./target/release/mixer")
context.log_level = 'debug'
r.recvuntil(b'Press enter to continue...\n')
r.sendline(b'')
for _ in range(1000):
    r.recvuntil(b"Input: ")
    n, string, numbers = r.recvline().split(b' | ')
    n = int(n)

    numbers = list(map(int, numbers.strip().split(b' ')))
    print(numbers)

    string = string.decode()
    numbers = list(map(lambda x: x - 1, numbers))
    result = ""
    for i in range(n):
        result = result + string[numbers[i]]
        # string = string[:i] + string[numbers[i]] + string[i + 1:]

    print(result)

    r.sendlineafter(b'Output: ', result.encode())

r.interactive()

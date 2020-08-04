from string import ascii_lowercase, digits

from pwn import *

s = remote('jh2i.com', 50009)
s.recvuntil("> ")

flag = ''

for i in range(1, 33):
    s.sendline('a' * (32 - i))
    base_block = re.findall('[a-f0-9]{64}', s.recvuntil("> ").decode('utf-8'))[0][:64]
    for c in '_{}' + ascii_lowercase + digits:
        s.sendline('a' * (32 - i) + flag + c)
        block = re.findall('[a-f0-9]{128}', s.recvuntil("> ").decode('utf-8'))[0][:64]
        if block == base_block:
            flag = flag + c
            print(flag)
            break

s.close()

# FLAG --> flag{aes_that_ick_ecb_mode_lolz}

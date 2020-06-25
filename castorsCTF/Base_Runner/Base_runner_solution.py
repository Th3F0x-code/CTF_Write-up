import base64
from pwn import *

def convert_base(num_list, base):
    converted = ""
    for num in num_list:
        converted += chr(int(num, base))

    return converted.split(" ")

def parse_binary(bin):
    # conversion
    base_2 = convert_base(bin, 2)
    base_8 = convert_base(base_2, 8)
    base_16 = convert_base(base_8, 16)
    return base64.b64decode(''.join(base_16))

p = remote('chals20.cybercastors.com', 14430)
p.sendline()
p.recvuntil("ready.\n")
received = p.recvuntil("\n")

# parse first message
received = received.split(b"\n")[0].split(b" ")
p.sendline(parse_binary(received))

for x in range(200):
    # continue until all questions are solved
    try:
        p.recvline()
        received = p.recvuntil("\n")
        received = received.split(b"\n")[0].split(b" ")
        p.sendline(parse_binary(received))
    except:
        break

# view flag
p.interactive()

from pwn import remote

HOST = "jh2i.com"
PORT = 50012
numbers = [0] * 100

i = 0

while True:
    if i == 0:
        r = remote(HOST, PORT)

    try:
        re = r.recvuntil(">")
    except Exception as e:
        r.interactive()
        continue

    print(re.decode(), end=" ")

    r.sendline(str(numbers[i]).encode())
    print(str(numbers[i]))

    print([i for i in numbers if i != 0])

    if numbers[i] == 0:
        res = r.recvuntil(".").decode()
        res += r.recv(1024).decode()
        numbers[i] = res.split("W A S ")[1].strip()
        i = 0
    else:
        i += 1
# FLAG --> flag{does_this_count_as_artificial_intelligence}

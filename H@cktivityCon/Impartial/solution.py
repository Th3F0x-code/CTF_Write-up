import re
import string

from pwn import remote

HOST = "jh2i.com"
PORT = 50026
r = remote(HOST, PORT)

flag = [''] + list('flag{') + ['?'] * 50

letters = list(string.ascii_lowercase + '_}1234567890')
tries = {i: letters for i in range(1, 51)}

# flag = [''] + list('flag{partial?pass?ord?puz?le?pieces????????????????????')
# flag{partial_password_puzzle_pieces}
for i in range(1, len(flag)):
    if flag[i] == '?':
        continue
    tries[i] = [flag[i]]

rec = r.recvuntil(">").decode()
print(rec, end=" ")

while True:
    res = b"2"
    r.sendline(res)
    print(res)

    rec = r.recvuntil("Username:").decode()
    print(rec, end=" ")

    res = b"admin"
    r.sendline(res)
    print(res)

    rec = r.recvuntil("Password:").decode()
    print(rec, end=" ")

    indices = [int(i) for i in re.findall(r'\d+', rec)]

    res = []

    for index in indices:
        res.append(tries[index][0])

    res = ' '.join(res)
    print(res)
    r.sendline(res)

    rec = r.recvuntil('>').decode()
    print(rec)

    if '1. Judge' in rec:
        r.sendline(b'3')
        print(''.join(flag))
        continue

    x = rec.split('1. About')[0].strip().split('\n')

    for i in range(len(x)):
        t = tries[indices[i]]
        if 'WRONG' in x[i]:
            tries[indices[i]] = t[1:]
        else:
            tries[indices[i]] = [t[0]]
            flag[indices[i]] = t[0]
    print(''.join(flag))

# FLAG --> flag{partial_password_puzzle_pieces}

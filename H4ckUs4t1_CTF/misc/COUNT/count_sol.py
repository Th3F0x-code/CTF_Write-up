from pwn import *


r = remote("ctf.hackusati.tech", 7015)

r.recvuntil(b"Let's start!\n")
cont = 0
while True:
    cont += 1
    print(cont)
    richiesta = r.recvline()
    if not b"Congratulations" in richiesta:
        print(richiesta)
        richiesta = richiesta.split()
        lettera = richiesta[2]
        parola = richiesta[4]
        lettera_count = parola.count(lettera)
        r.sendline(str(lettera_count))
        r.recvline()
    else:
        print(r.recvline())
        print(r.recvline())
r.interactive()

# flag --> ITT{pyth0n_1s_us3ful}

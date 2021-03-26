from pwn import *

r = remote("2048.challs.olicyber.it", 10007)
r.recvline()
r.recvline()

with log.progress("Solving operation") as l:
    for _ in range(2048):
        l.status(f"{_}/2048")
        line = r.recv().split()
        if line[0] == b"SOMMA":
            r.sendline(str(int(line[1]) + int(line[2])))
        elif line[0] == b"POTENZA":
            r.sendline(str(int(line[1]) ** int(line[2])))
        elif line[0] == b"DIVISIONE_INTERA":
            r.sendline(str(int(line[1]) // int(line[2])))
        elif line[0] == b"DIFFERENZA":
            r.sendline(str(int(line[1]) - int(line[2])))
        elif line[0] == b"PRODOTTO":
            r.sendline(str(int(line[1]) * int(line[2])))

    r.recvuntil("Congratulazioni: ")
    l.success(r.recvline())
    r.close()

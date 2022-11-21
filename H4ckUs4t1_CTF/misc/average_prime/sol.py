from pwn import *

r = remote("ctf.hackusati.tech", 7025)
cont=0
r.recvuntil(b"Every list has at least one prime number\n")
while True:
    cont+=1
    print("Iterazione numero",cont)
    print(r.recvline())
    richiesta = []
    richiesta = r.recvline().split()

    #casting vari
    richiesta = list(filter(lambda x: x!= b' and ',richiesta))
    richiesta = list(filter(lambda x: x!= b',',richiesta))
    #casting vari
    for i in range(len(richiesta)):
        richiesta[i] = richiesta[i].decode("utf-8")
        richiesta[i] =richiesta[i][:-1]
    richiesta[0] = richiesta[0][1:]
    
    #converto ad intero
    for i in range(len(richiesta)):
        richiesta[i] = int(richiesta[i])
    print(richiesta)
    
    #estraggo i numeri primi 
    prime_numbers = []
    for i in richiesta:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    print(prime_numbers)
    #
    #calcolo la media
    media = int(sum(prime_numbers) / len(prime_numbers))
    print("media intera",media)
    #send answer
    r.sendline(str(media))
    print(r.recv())

    print(r.recvline())
    


r.interactive()
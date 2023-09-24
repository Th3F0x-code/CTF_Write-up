from pwn import *

r = process("./target/release/twoforyou")
# set log level to debug
context.log_level = 'debug'
r.recvuntil(b'Press enter to continue...\n')
r.sendline(b'')
for _ in range(1000):
    r.recvuntil(b"Input: ")
    n = r.recvline().strip()
    '''    let mut output = String::new();
    let mut i = 1;
    while i <= 10 {
        output.push_str(&(random_number * i).to_string());
        output.push_str(" ");
        i += 1;
    }'''
    n = int(n)
    sol = ''
    for i in range(1, 11):
        sol += str(n * i) + ' '

    # print(n)
    # print(sol)
    r.sendlineafter(b'Output: ', sol)
    #print(r.recvline())

r.interactive()

'''
83161 166322 249483 332644 415805 498966 582127 665288 748449 831610 

83161 166322 249483 332644 415805 498966 582127 665288 748449 831610 

'''

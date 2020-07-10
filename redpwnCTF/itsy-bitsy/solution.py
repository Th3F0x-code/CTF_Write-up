from pwn import remote
ans = '11'
for i in range(2, 301): 
    p = remote('2020.redpwnc.tf', 31284) 
    p.read() 
    p.write(f'{i-1}\n') 
    p.read() 
    p.write(f'{i}\n') 
    ret1 = p.read() 
    ret = ret1[12:313] 
    ans += chr(ret[i] ^ 1) 
    p.close()
print(''.join([chr(int(ans[i:i+7], 2)) for i in range(0, 301, 7)]))

#FLAG --> flag{bits_leaking_out_down_the_water_spout}

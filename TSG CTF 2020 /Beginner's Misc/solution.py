from pwn import *

conn = remote("35.221.81.216", 30718)

table = {
    '0.1/': "㝿㝴",
    'e00+': '{M>',
    'e01+': '{M~',
    'e04+': '{N>',
    'e05+': '{N~',
    'e08+': '{O>',
    'e09+': '{O~',
    'e10+': '{]>',
    'e11+': '{]~',
    'e013': '{Mw',
    'e14+': '{^>',
    'e15+': '{^~',
}

payload = "0.1/e00+" * 31
payload += "0.1/e01+" * 4
payload += "0.1/e04+" * 159
payload += "0.1/e05+" * 2
payload += "0.1/e08+" * 653
payload += "0.1/e09+" * 5
payload += "0.1/e10+" * 8
payload += "0.1/e11+" * 9
payload += "0.1/e14+" * 807
payload += "0.1/e013"

data = ""
for i in range(0, len(payload), 4):
    data += table[payload[i:i + 4]]

conn.sendlineafter("? ", data)
conn.interactive()

# FLAG -->TSGCTF{Y0u_t00k_the_first_step_0f_the_misc_w0rld!_G0_and_s0lve_all_the_remaining_challenges}

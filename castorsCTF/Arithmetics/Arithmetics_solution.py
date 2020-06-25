from pwn import *

r = remote("chals20.cybercastors.com", 14429)

# skip description
r.recvuntil("ready.")
r.recvline()
r.sendline()

nums = {'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'}

multipliers = {
    'minus': '-',
    'plus': '+',
    'multiplied-by': '*',
    'divided-by': '//'
}

for i in range(100):
    r.recvuntil("is ")
    # sanitize operation to get only essentials
    query = str(r.recvuntil("?")[:-2]).replace("b'", '').replace("'", '').split(" ")
    
    # dirty-but-it-works-method of replacing spelled-out numbers with real ones.
    if query[0] in nums:
        query[0] = nums[query[0]]
    if query[-1] in nums:
        query[-1] = nums[query[-1]]
    if query[1] in multipliers:
        query[1] = multipliers[query[1]]
    # eval expression and send back
    r.sendline(str(eval(" ".join(query))))

r.interactive()

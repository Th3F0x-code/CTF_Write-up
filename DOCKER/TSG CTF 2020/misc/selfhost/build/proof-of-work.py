#!/usr/bin/env python3
from random import choice
from string import *
import signal
from os import system
import sys

def handler(x, y):
    sys.exit(1)


signal.signal(signal.SIGALRM, handler)
signal.alarm(60)

LENGTH = 9
STRENGTH = 27
def gen_randstr(length=LENGTH):
    return ''.join((choice(ascii_lowercase) for i in range(length)))

def main():
    s = gen_randstr()
    print("[Proof of Work]")
    print("Submit the token generated by `hashcash -mb{} {}`".format(STRENGTH, s))
    ans = input()
    ans_chrs = ascii_letters + digits + ":/+"
    l = list(filter(lambda c: c not in ans_chrs, ans))
    if len(l) != 0:
        exit(1)
    r = system("hashcash -cdb{} -f /hashcash/hashdb -r {} {}".format(STRENGTH, s, ans))
    exit(0 if r == 0 else 1)

main()

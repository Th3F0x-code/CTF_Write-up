from pwn import *
import string
import secrets

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


# create a list with all the chars
chars="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{}"

while True:
    elf=ELF("./flag_checker")
    for c in chars:
    p=elf.process( ["./flag_checker", ] )
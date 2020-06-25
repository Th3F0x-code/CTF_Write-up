from Crypto.Util.number import *
from gmpy2 import c_div
from pwn import *

# decrypt(encrypt(FLAG) * encrypt(2)) == 2*FLAG

r = remote('149.202.200.158', 7011)

r.recvuntil('flag: ')
flag_encrypted = r.recvline().decode()[0:-1]

r.sendlineafter('> ', str('1'))

r.sendlineafter('Plaintext > ', str('2'))

r.recvuntil('Encrypted: ')
two_encrypted = r.recvline().decode()[0:-1]

flag_two_encrypt = int(flag_encrypted) * int(two_encrypted)

r.sendlineafter('> ', str('2'))

r.sendlineafter('Ciphertext > ', str(flag_two_encrypt))

r.recvuntil('Decrypted: ')
flag_two_decrypt = r.recvline().decode()[0:-1]

encrypted_flag = c_div(int(flag_two_decrypt), 2)
print('Flag:', long_to_bytes(encrypted_flag).decode())

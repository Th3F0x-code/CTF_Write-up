#!/usr/bin/python3

import base64
import string
import time
from itertools import product

m = "See you later in the city center"
c = "QSldSTQ7HkpIJj9cQBY3VUhbQ01HXD9VRBVYSkE6UWRQS0NHRVE3VUQrTDE="


def decrypt(enc, key):
    dec = []
    enc = str(base64.urlsafe_b64decode(enc.encode('ascii')), 'ascii')
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((128 + ord(enc[i]) - ord(key_c)) % 128)
        dec.append(dec_c)
    return "".join(dec)


def encrypt(clear, key):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 128)
        enc.append(enc_c)
    return str(base64.urlsafe_b64encode("".join(enc).encode('ascii')), 'ascii')


start = time.time()

print("Find all key.")
key_table = [''.join(_) for _ in product(string.ascii_lowercase, repeat=4)]

print("Fill the encrypt table.")
encrypt_table = [encrypt(m, key_one) for key_one in key_table]

print("Fill the decrypt table.")
decrypt_table = [decrypt(c, key_due) for key_due in key_table]

print("Searching the flag.")
intersect = set(encrypt_table).intersection(set(decrypt_table))

for _in in intersect:
    print("Flag: CCIT{%s}" % (key_table[encrypt_table.index(_in)] + key_table[decrypt_table.index(_in)]))

end = time.time()
print(f"Tempo impiegato: {end - start} sec.")

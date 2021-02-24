import base64
import string
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


print("Find all key.")
# Riempio una lista con tutte le combinazioni possibili di lunghezza 4 che posso fare con le lettere a...z (aaaa, abbb, abca, ahca..).
key_table = [''.join(_) for _ in product(string.ascii_lowercase, repeat=4)]

print("Fill the encrypt table.")
# Riempio la lista con tutti messaggi 'm' cifrati da tutte le key presenti nella lista.
encrypt_table = [encrypt(m, key_one) for key_one in key_table]

print("Fill the decrypt table.")
# Riempio la lista con tutti messaggi 'c' decifrati da tutte le key presenti nella lista.
decrypt_table = [decrypt(c, key_due) for key_due in key_table]

print("Searching the flag.")
# Interseco le due liste e ritorno gli elementi in comune in una collection, ovvero encrypt(m) == decrypt(c).
intersect = set(encrypt_table).intersection(set(decrypt_table))  # {'SEtUFW5VZBVhR2NaZwZYYxVaV1oVSVhpbgZSWmNaVGc='}

# Con 'encrypt_table.index(_in)' ritorno l'indice in cui si trova l'elemento della collection che corrisponde alla key con cui è stato effettuato l'encrypt.
# Vale lo stesso ragionamento per l'altra lista.
for _in in intersect:
    # key_table[encrypt_table.index(_in)] -> ufou, key_table[decrypt_table.index(_in)] -> ndit.
    print("Flag: CCIT{%s}" % (key_table[encrypt_table.index(_in)] + key_table[decrypt_table.index(_in)]))

# FLAG --> CCIT{ufoundit}

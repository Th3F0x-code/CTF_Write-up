import base64
import time
from hashlib import md5


def xor(data, key):
    return bytearray(a ^ b for a, b in zip(*map(bytearray, [data, key])))


timestamp_initial = int(time.time())
with open('noob.txt', 'r') as ct_file:
    ct = ct_file.read().strip()

ct = base64.b64decode(ct)

for i in range(1000000):
    timestamp = timestamp_initial - i
    key = md5(str(int(timestamp)).encode()).hexdigest()
    my_hexdata = key
    scale = 16
    num_of_bits = 8
    noobda = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
    xorer = xor(ct, noobda)
    if b'batpwn{' in xorer and b'}' in xorer:
        print(xorer)

# batpwn{cryptography_is_beautiful_art}

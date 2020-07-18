import math
from base64 import b64encode

exploit = input('? ')

if eval(b64encode(exploit.encode('UTF-8'))) == math.pi:
    print("flag")

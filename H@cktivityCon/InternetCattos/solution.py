import socket
import time

HOST = "jh2i.com"
PORT = 50003
sock = socket.socket()
sock.connect((HOST, PORT))
time.sleep(1)
data = sock.recv(1024).replace(b'\r', b'').decode()
print(data)

# FLAG --> flag{this_netcat_says_meow}

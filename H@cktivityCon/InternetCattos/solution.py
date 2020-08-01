import socket
import time

sock = socket.socket()
sock.connect(('jh2i.com', 50003))
time.sleep(1)
data = sock.recv(1024).replace(b'\r', b'').decode()
print(data)

# FLAG --> flag{this_netcat_says_meow}

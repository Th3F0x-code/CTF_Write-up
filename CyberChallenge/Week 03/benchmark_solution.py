import socket
import time


def netcat(hn, p, content):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hn, p))

    sock.sendall(content.encode())
    time.sleep(0.5)
    sock.shutdown(socket.SHUT_WR)

    res = ""

    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()

    print(res.split(' ')[-8])
    print("Connection closed.")
    sock.close()
    return res.split(' ')[-8]


if __name__ == '__main__':
    charset = [chr(i) for i in range(33, 127)]
    keysofar = "CCIT{s1d"
    host = "149.202.200.158"
    port = 7001
    res = []
    maximum = None

    while maximum != '}':
        for c in charset:
            res.append((int(netcat(host, port, keysofar + c)), c))

        print("max val")
        maximum = max(res, key=lambda x: x[0])[1]
        keysofar = keysofar + maximum
        print(keysofar)

# FLAG -->  CCIT{s1d3_ch4nn3ls_r_c00l

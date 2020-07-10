import hashlib
import socket


def readln(sock):
    r = b""
    while True:
        c = sock.recv(1)
        if c != b'\n':
            r += c
        else:
            break
    return r


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('challs.m0lecon.it', 10002))
received = clientsocket.recv(4096)
clientsocket.send(
    (hashlib.md5(received.decode().split("\n")[0].split(" ")[2].encode('utf-8')).hexdigest() + "\n").encode())
for i in range(21):
    received = readln(clientsocket)
while True:
    num = int(readln(clientsocket))
    table = []
    seta = []
    setb = []
    ops = readln(clientsocket).decode("utf-8").split(" ")
    readln(clientsocket)
    for i in range(num):
        table.append(readln(clientsocket).decode("utf-8").split(" "))
    anum = int(readln(clientsocket))
    for i in range(anum):
        seta.append(readln(clientsocket).decode("utf-8").split(" "))
    bnum = int(readln(clientsocket))
    for i in range(bnum):
        setb.append(readln(clientsocket).decode("utf-8").split(" "))
    mapping = [-1 for _ in range(len(ops))]
    n = len(ops)
    identity = table.index(ops)
    mapping[identity] = 0
    if identity == 0:
        oneel = 1
    else:
        oneel = 0
    mapping[oneel] = 1
    curr = oneel
    num = 1
    while num < len(ops) - 1:
        num += 1
        curr = ops.index(table[oneel][curr])
        mapping[curr] = num


    def getVal(emoj):
        return mapping[ops.index(emoj)]


    opsnum = [getVal(x) for x in ops]
    tabnum = [[getVal(x) for x in y] for y in table]
    setanum = [[getVal(x) for x in y] for y in seta]
    setbnum = [[getVal(x) for x in y] for y in setb]


    def transpose(m):
        return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


    setanumt = transpose(setanum)
    setbnumt = transpose(setbnum)
    x = mapping[ops.index(chr(128514))]
    mat = [setanumt[0] + [0 for _ in range(len(setanumt[0]))]] + [setanumt[i] + list(map(lambda x: -x, setbnumt[i])) for
                                                                  i in range(len(setanumt))]
    vec = [x] + [0 for _ in range(len(mat) - 1)]
    A = Matrix(GF(n), mat)
    b = Matrix(GF(n), vec).transpose()
    v0 = A.solve_right(b)
    vals = v0[:len(setanum)]
    ans = " ".join(ops[mapping.index(sum(vals[i][0] * setanum[i][j] for i in range(len(setanum))) % n)] for j in
                   range(len(setanum[0])))
    clientsocket.send((ans + "\n").encode())
    print(readln(clientsocket).decode("utf-8"))

# FLAG --> ptm{V3ct0r_m4th_w1th_3m0ji1_i5_fun}

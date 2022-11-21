#!/bin/python3

import os
import json
import sys

with open("port_config.json") as json_file:
    port_config = json.load(json_file)

port_config = {**port_config["crypto"], **port_config["misc"], **port_config["pwn"], **port_config["web"], **port_config["reverse"]}


def build(challenge=None):
    if challenge is None:
        for root, dirs, files in os.walk("."):
            if root.count(os.sep) == 2 and os.path.exists(root + "/Dockerfile"):
                name = os.path.basename(root).lower()
                os.system(f"docker build -t {name} {root}")
    else:
        for root, dirs, files in os.walk("."):
            if os.path.basename(root).lower() == challenge.lower() and root.count(os.sep) == 2 and os.path.exists(
                    root + "/Dockerfile"):
                name = os.path.basename(root).lower()
                os.system(f"docker build -t {name} {root}")


def run(challenge=None):
    if challenge is None:
        for name, port in port_config.items():
            if port != "":
                os.system(f"docker run --rm -d -p {port} {name}")
            else:
                os.system(f"docker run --rm -d {name}")
    else:
        for name, port in port_config.items():
            if name.lower() != challenge.lower():
                continue

            if port != "":
                os.system(f"docker run --rm -d -p {port} {name}")
            else:
                os.system(f"docker run --rm -d {name}")


def kill(challenge=None):
    if challenge is None:
        os.system("docker kill $(docker ps -q)")
    else:
        os.system(f"docker kill $(docker ps -a -q --filter ancestor={challenge})")


def restart(challenge=None):
    kill(challenge)
    run(challenge)
    # if challenge is None:
    #     os.system("docker restart $(docker ps -q)")
    # else:
    #     os.system(f"docker restart $(docker ps -a -q --filter ancestor={challenge})")


def print_usage():
    print("Usage: python handle_containers.py [action] [optional: challenge name]")
    print()
    print("Actions:")
    print("-b   --build     build a specific container or all container if none specified")
    print("-s   --run       run a specific container or all container if none specified")
    print("-k   --kill      kill a specific container or all container if none specified")
    print("-r   --restart   restart all containers")


challenge = None if len(sys.argv) < 3 else sys.argv[2]

if len(sys.argv) < 2:
    print_usage()
    exit()

if sys.argv[1] == "--build" or sys.argv[1] == "-b":
    build(challenge)
elif sys.argv[1] == "--run" or sys.argv[1] == "-s":
    run(challenge)
elif sys.argv[1] == "--kill" or sys.argv[1] == "-k":
    kill(challenge)
elif sys.argv[1] == "--restart" or sys.argv[1] == "-r":
    restart(challenge)
else:
    print_usage()

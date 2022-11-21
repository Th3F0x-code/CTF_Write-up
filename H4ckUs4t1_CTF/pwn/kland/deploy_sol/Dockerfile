FROM ubuntu:18.04

RUN apt update && apt upgrade -y && apt install -y python python-pip make gcc && rm -rf /var/lib/apt/lists/*
RUN pip install pwntools

RUN mkdir /home/ctf
WORKDIR /home/ctf
RUN useradd -M -d /home/ctf ctf

COPY ./bin/ /home/ctf/

ENTRYPOINT [ "/bin/sh", "-c", "python solve.py" ]
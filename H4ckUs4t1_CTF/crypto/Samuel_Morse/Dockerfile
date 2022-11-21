FROM ubuntu:16.04
RUN apt update -y && apt upgrade -y && apt install -y lib32z1 \
    socat \
    gcc \
    libc6-dev-i386 

RUN useradd -m ctf
WORKDIR /ctf

COPY chall.c .
COPY flag.txt .


RUN gcc -s -O3 -static chall.c -o server
EXPOSE 7017

ENTRYPOINT ["/bin/sh", "-c", "socat TCP-LISTEN:7017,fork,reuseaddr EXEC:./server"]


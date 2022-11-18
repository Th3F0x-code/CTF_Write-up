FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y \
    lib32z1 \
    socat \
    gcc \
    libc6-dev-i386 \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf

WORKDIR /ctf
COPY chall.c .
COPY libc-2.23.so .
COPY flag.txt .
COPY run.sh .


RUN gcc -fno-stack-protector -g1 -no-pie -m32 chall.c -o ret2school
RUN rm chall.c

EXPOSE 7003

ENTRYPOINT ["/bin/sh", "-c", "socat TCP-LISTEN:7003,fork,reuseaddr EXEC:./run.sh"]

# 7003:7003
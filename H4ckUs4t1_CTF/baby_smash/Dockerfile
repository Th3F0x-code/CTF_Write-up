FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y \
    lib32z1 \
    socat \
    libc6-dev-i386 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf

WORKDIR /ctf
COPY flag.txt .
COPY chall.c .

RUN gcc -fno-stack-protector -g1 -no-pie -m32  chall.c -o baby_smash
RUN rm chall.c

EXPOSE 7000

ENTRYPOINT ["/bin/sh", "-c", "socat TCP-LISTEN:7000,fork,reuseaddr EXEC:./baby_smash"]

# 7000:7000
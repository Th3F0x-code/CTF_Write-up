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
COPY main.c .

RUN gcc main.c -o inty_integer
RUN rm main.c

EXPOSE 7001  #change me

ENTRYPOINT ["/bin/sh", "-c", "socat TCP-LISTEN:7001,fork,reuseaddr EXEC:./ez_jmp"]

# 7001:7001
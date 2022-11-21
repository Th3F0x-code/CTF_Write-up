FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y \
    lib32z1 \
    socat \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf

WORKDIR /ctf
COPY chall.c .

RUN gcc -g1 chall.c -o format_me
RUN rm chall.c

EXPOSE 7002

ENTRYPOINT ["/bin/sh", "-c", "socat TCP-LISTEN:7002,fork,reuseaddr EXEC:./format_me"]

# 7002:7002
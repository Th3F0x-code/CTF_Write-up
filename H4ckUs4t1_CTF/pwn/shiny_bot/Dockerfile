FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y \
    lib32z1 \
    socat \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf

WORKDIR /ctf
COPY chall.c .
COPY libc.so.6 .
COPY flag.txt .
COPY run.sh .



RUN gcc  -g1 -Wl,-z,relro,-z,now chall.c -o shiny_bot
RUN rm chall.c

EXPOSE 7004

ENTRYPOINT ["/bin/sh", "-c", "socat TCP-LISTEN:7004,fork,reuseaddr EXEC:./run.sh"]

# 7004:7004
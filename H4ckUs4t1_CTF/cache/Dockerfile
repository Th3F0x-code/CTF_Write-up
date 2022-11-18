FROM ubuntu:18.04

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install lib32z1 \
    socat \
    gcc \
    && rm -rf /var/lib/apt/lists/*


RUN useradd -m ctf

WORKDIR /ctf

COPY chall.c .
COPY libc-2.27.so .
COPY start.sh .
COPY flag.txt .

RUN gcc -g -O0 -Wl,-z,relro,-z,now -no-pie -o cache chall.c
RUN rm chall.c
RUN chmod +x start.sh

EXPOSE 7005
ENTRYPOINT ["/bin/sh", "-c", "socat TCP-LISTEN:7005,fork,reuseaddr EXEC:./start.sh"]


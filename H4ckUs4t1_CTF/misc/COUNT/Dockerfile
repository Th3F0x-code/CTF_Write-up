FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y \
    lib32z1 \
    socat \
    python3 \ 
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf

WORKDIR /ctf
COPY . .



EXPOSE 7015

ENTRYPOINT ["/bin/sh", "-c", "socat TCP-LISTEN:7015,fork,reuseaddr EXEC:./run.sh"]

# 7015:7015
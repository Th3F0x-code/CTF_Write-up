FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y \
        socat && \
    apt-get clean


RUN useradd -m ctf

WORKDIR /home/ctf

COPY fibonacci .
COPY flag.txt .
EXPOSE 7024

ENTRYPOINT ["/bin/sh", "-c", "socat TCP-LISTEN:7024,fork,reuseaddr EXEC:./fibonacci"]

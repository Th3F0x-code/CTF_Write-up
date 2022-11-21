FROM python:3.7-slim

RUN apt-get update && apt-get install -y \
  socat \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /ctf
WORKDIR /ctf
RUN useradd -M -d /ctf ctf
COPY flag.txt . 
COPY start.sh .
COPY chall.py .

EXPOSE 7016

ENTRYPOINT ["/bin/sh", "-c", "socat TCP-LISTEN:7016,fork,reuseaddr EXEC:./start.sh"]
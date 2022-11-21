FROM ubuntu:latest

RUN apt update && \
    apt upgrade -y && \
    apt install -y python3 python3-pip socat \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf

WORKDIR /ctf

COPY ./arithmetic_average.py .
COPY ./flag.txt .
COPY ./start.sh .

RUN chmod +x start.sh

EXPOSE 7025
ENTRYPOINT ["/bin/sh", "-c", "socat TCP-LISTEN:7025,fork,reuseaddr EXEC:./start.sh"]

# sudo docker build -t <nome> <directory>
# sudo docker run -d -p <port out: port in> --rm -it <nome>

FROM ubuntu:19.10

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY <binary> .
COPY ynetd .

RUN chown -R root:root /home/ctf

USER ctf
EXPOSE <exposed port>
CMD ./ynetd -p <port> <binary to execute>

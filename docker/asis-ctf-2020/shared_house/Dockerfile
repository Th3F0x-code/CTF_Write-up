FROM ubuntu:18.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get update && apt-get install -y lib32z1 xinetd build-essential
RUN apt-get install -y qemu && apt-get install -y qemu-system

RUN echo 'pwn - nproc 1500' >> /etc/security/limits.conf

RUN useradd -m pwn
WORKDIR /home/pwn

ADD challenge/init.sh    /etc/init.sh
RUN chmod 550 /etc/init.sh

ADD challenge/qemu/bzImage     /home/pwn
ADD challenge/qemu/rootfs.cpio /home/pwn
ADD challenge/pwn.xinetd       /etc/xinetd.d/pwn
ADD challenge/qemu/start.sh    /home/pwn

RUN chmod 550 /home/pwn/*

RUN service xinetd restart

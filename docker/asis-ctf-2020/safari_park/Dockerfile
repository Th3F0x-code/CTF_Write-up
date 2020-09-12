FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update --fix-missing && apt-get -y upgrade
RUN apt-get -y install xinetd
RUN apt-get -y install python3.7
RUN apt-get -y install libicu60
RUN groupadd -r pwn && useradd -r -g pwn pwn

ADD challenge/pwn.xinetd /etc/xinetd.d/pwn
ADD challenge/init.sh    /etc/init.sh
ADD challenge/server.py  /home/pwn/server.py
RUN chmod 550  /home/pwn/server.py
RUN chmod 500  /etc/init.sh
RUN chmod 1733 /tmp /var/tmp /dev/shm

ADD challenge/flag.txt                       /flag-lemurcatta.txt
ADD distfiles/release/jsc                    /home/pwn/
ADD distfiles/release/libJavaScriptCore.so.1 /usr/lib/x86_64-linux-gnu/
RUN chmod 444 /flag-lemurcatta.txt
RUN chmod 550 /home/pwn/jsc
RUN chmod 555 /usr/lib/x86_64-linux-gnu/libJavaScriptCore.so.1

RUN chown -R root:pwn /home/pwn

RUN service xinetd restart

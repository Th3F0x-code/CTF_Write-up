FROM ubuntu:18.04

RUN apt-get clean
RUN apt-get update
RUN apt-get install -y python python-pip


RUN pip install pwntools pathlib2

COPY exploit.py /exploit.py
COPY exploit.gz.b64 /exploit.gz.b64

ENTRYPOINT ["python2", "/exploit.py"]

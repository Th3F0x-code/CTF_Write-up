FROM ubuntu:18.04
COPY requirements.txt install.sh /root/
COPY ./service /root/service
RUN bash /root/install.sh
CMD /home/aircnc/venv/bin/python3 /home/aircnc/FlightRecorder --config /etc/aircnc.yaml --debug --username flight14 --password a7ccfcd563ef2f85286578c4a8a4a381

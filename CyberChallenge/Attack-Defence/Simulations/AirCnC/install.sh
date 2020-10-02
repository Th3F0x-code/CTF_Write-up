#!/bin/bash

cd /root
useradd -m -s /bin/bash aircnc
chmod 770 /home/aircnc
mv service/FlightRecorder /home/aircnc/
mv service/config.yaml /etc/aircnc.yaml
mv requirements.txt /home/aircnc
chown aircnc:aircnc -R /home/aircnc
chown root:root /etc/aircnc.yaml
chmod 770 /home/aircnc/FlightRecorder
chmod 664 /etc/aircnc.yaml

apt-get update -y && apt-get install -y python3-venv zstd
su -c "cd /home/aircnc && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && rm requirements.txt"

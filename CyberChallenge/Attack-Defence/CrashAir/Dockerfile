FROM ubuntu:18.04
RUN apt-get update && apt-get install -y build-essential python3-dev python3-setuptools python3-pip virtualenv uwsgi uwsgi-plugin-python3 nginx

RUN useradd -U -m -s /bin/bash crashair

COPY ./bottle.ini /etc/uwsgi/apps-available/bottle.ini
RUN ln -fs /etc/uwsgi/apps-available/bottle.ini /etc/uwsgi/apps-enabled/bottle.ini
COPY ./bottle.conf /etc/nginx/sites-enabled/
RUN rm /etc/nginx/sites-enabled/default

COPY ./src /home/crashair
RUN chown -R crashair:crashair /home/crashair

USER crashair
WORKDIR /home/crashair

RUN virtualenv --python=python3 /home/crashair/venv
RUN . venv/bin/activate; pip install bottle
USER root
CMD service uwsgi start 2>&1 >/dev/null; nginx -g 'daemon off;' -c /etc/nginx/nginx.conf

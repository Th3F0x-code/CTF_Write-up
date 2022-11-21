FROM nginx:latest

COPY src /usr/share/nginx/html
COPY nginx.conf .

RUN mv nginx.conf /etc/nginx/nginx.conf

EXPOSE 7008

# 7008:7008
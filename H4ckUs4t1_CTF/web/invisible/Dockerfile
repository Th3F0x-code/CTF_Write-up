FROM nginx:latest

COPY src /usr/share/nginx/html
COPY nginx.conf .

RUN mv nginx.conf /etc/nginx/nginx.conf

EXPOSE 7009

#7009:7009
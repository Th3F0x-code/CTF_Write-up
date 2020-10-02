FROM mysql:8.0.21
ENV MYSQL_RANDOM_ROOT_PASSWORD=true
COPY ./db/init.sql /docker-entrypoint-initdb.d/
COPY ./htdocs /root/htdocs/
COPY ./install.sh /root/
RUN chmod 666 /docker-entrypoint-initdb.d/*
WORKDIR /root
RUN chmod +x /root/*.sh; /root/install.sh
CMD service php7.3-fpm start; service nginx restart; docker-entrypoint.sh mysqld --default-authentication-plugin=mysql_native_password

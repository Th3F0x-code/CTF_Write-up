#!/bin/bash

apt update
yes | apt install nginx
yes | apt install php-fpm php-mysql

# write conf
# be careful with the $ signs so use heredocs with no substitution
cat << 'EOF' > /etc/nginx/sites-available/lph 
server {
    listen 80 default_server;
    root /var/www/lph/htdocs;
    index index.php index.html index.htm index.nginx-debian.html;
    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ \.php$ {
      include snippets/fastcgi-php.conf;
      fastcgi_pass unix:/var/run/php/php7.3-fpm.sock;
    }

    location ~ /\.ht {
      deny all;
    }
}

EOF
# activate site
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/lph /etc/nginx/sites-enabled/lph
mkdir -p /var/www/lph/

# remember to change host db to localhost in config.inc.php
sed -i -e 's/mysql/localhost/g' htdocs/includes/config.inc.php

# copy files
cp -r htdocs /var/www/lph/
chown -R root:www-data /var/www/lph
chmod -R 774 /var/www/lph 


#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
locat_n="\
    location /hbnb_static {\n\
        alias /data/web_static/current/;\n\
    }\n\
"
sudo sed -i "/listen 80 default_server/a $locat_n" /etc/nginx/sites-enabled/default
sudo service nginx start

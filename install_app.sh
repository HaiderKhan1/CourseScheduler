#!/bin/bash
APP_PATH="./project"
apt update && apt upgrade
pushd $APP_PATH

# install node packages
apt install nodejs npm
pushd frontend && npm install react-router-dom --save && npm install && npm run build && popd
# install python packages
apt install python3.10-venv
pushd backend && python3 -m venv env && source env/bin/activate && pip install -r requirements.txt
# Configure Gunicorn and Nginx
apt-get install nginx
touch /etc/nginx/sites-available/flask_server
echo "server {listen 80;server_name 34.130.250.108;location / {proxy_pass http://10.188.0.4:5000;}}" >> /etc/nginx/sites-available/flask_server
cd /etc/nginx/sites-enabled
ln -s /etc/nginx/sites-available/flask_server
cd /etc/systemd/system
touch flask_server_service.service
echo -e "[Unit]\nDescription= Flask Server\nAfter=network.target\n[Service]\nUser=root\nGroup=www-data\nExecStart=/home/$USER/3760project/project/backend/env/bin/gunicorn --bind 0.0.0.0:5000 --reload\n[Install]\nWantedBy=multi-user.target" >> /etc/systemd/system/flask_server_service.service
systemctl enable flask_server_service
systemctl start flask_server_service

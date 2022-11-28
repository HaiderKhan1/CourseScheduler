#!/bin/bash

pushd project/frontend && npm run build && cp -R ./build/* /var/www/CIS3760project/html
systemctl restart nginx

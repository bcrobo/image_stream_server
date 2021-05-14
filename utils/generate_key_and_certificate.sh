#!/bin/bash

# Manual SSL certificate, but not recognized by a CA
# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

# Using let's encrypt
# sudo letsencrypt certonly --dry-run --manual --email bruno.celaries@gmail.com -d home-network.hd.free.fr


# - Congratulations! Your certificate and chain have been saved at:
#    /etc/letsencrypt/live/home-network.hd.free.fr/fullchain.pem
#    Your key file has been saved at:
#      /etc/letsencrypt/live/home-network.hd.free.fr/privkey.pem
#    Your cert will expire on 2021-08-01. To obtain a new or tweaked
#    version of this certificate in the future, simply run certbot
#    again. To non-interactively renew *all* of your certificates, run "certbot renew"



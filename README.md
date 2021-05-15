# Image stream server

## Abstract

`image_stream_server` is a ROS node that wraps a python Flask web server. It is designed to offer a very simple web interface for the different ROS projects. The following sections described the different steps to perform to setup up the web server. The first two sections might differ depending on your ISP (Internet Service Provider) but aren't necessary if you want to keep your web server within you local network. However, if you want to access that server from the world wide web you will need them.

Third 

## 1. Ask to your ISP a static ip (remote access only)

Most of ISPs use an ip to represent several routers. Each of them has a virtual ip, that is used to route the traffic that this specific to that router. I'm using `Free` (a french ISP) and in your customer account you can enable this option and restart your router. You can find this option from the `MAFREEBOX > Demander une IP fixe V4 Full Stack`. Now you router has a unique ip that is reachable on the world wide web even if it restarts its IP will remain unchanged.

## 2. Ask to your ISP a DNS (remote access only)

Some internet provider offer a DNS service that can be used for your web application. A DNS (Domain Name Service) resolves your router ip to a specific name. `Free`  provides this option and you can choose a name for your server (if it is not already in use). Go into the `MAFREEBOX > Personnaliser mon reverse DNS` then at the bottom of the page, enter a name for your server in the field `Reverse DNS personnalisé`. For instance my server name is `xxxxxx.hd.freebox.fr`. 

## 3. Use Nginx server as reverse proxy

[Nginx](https://www.nginx.com/) server is another web server. Compared to `Flask`, `Nginx` is production oriented server. However, `Flask` is very practical for prototyping and hobbies. Using `Nginx` as a reverse proxy allow to dedicate the SSL security to `Nginx` while keeping the content in under the `Flask` scope.
Under is a small diagram that explain what's happening when you try to reach the server:



## 4. Ask a SSL certificate from LetsEncrypt entity (remote access only)

[LetsEncrypt](https://letsencrypt.org/) is a nonprofit certificate authority. You can ask for a certificate using their utility program `certbot`. Its installation is very simple `sudo apt-get install certbot`.

# Image stream server

## Abstract

`image_stream_server` is a ROS node that wraps a python Flask web server. It is designed to offer a very simple web interface for the different ROS projects. The following sections described the step to perform the setup of the web server.

## 1. Ask to your internet provider a static ip (remote access only)

Most of internet providers use an ip to represent several routers. Each of them has a virtual ip, that is used to route the traffic that this specific to one router. I'm using Free internet provider and in you customer account you can enable this option and restart your router. Now you router has a unique ip that is reachable on the world wide web.

## 2. Ask to your internet provider a DNS (remote access only)

Some internet provider offer a DNS service that can be used for your web application. A DNS (Domain Name Service) resolves your router ip to a specific name. Free  provides this option and you can choose a name for your server (is it is not already in use). For instance my server name is `xxxxxx.hd.freebox.fr`. 

## 3. 


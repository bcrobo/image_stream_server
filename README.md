# Image stream server

## Abstract

`image_stream_server` is a ROS node that wraps a python Flask web server. It is designed to offer a very simple web interface for the different ROS projects. The following sections described the different steps to perform to setup up the web server. The first two sections might differ depending on your ISP (Internet Service Provider) but aren't necessary if you want to keep your web server within you local network. However, if you want to access that server from the world wide web you will need them.

Third 

## 1. Web application remote access
### 1.1 Ask to your ISP a static ip

Most of ISPs use an ip to represent several routers. Each of them has a virtual ip, that is used to route the traffic that this specific to that router. I'm using `Free` (a french ISP) and in your customer account you can enable this option and restart your router. You can find this option from the `MAFREEBOX > Demander une IP fixe V4 Full Stack`. Now you router has a unique ip that is reachable on the world wide web even if it restarts its IP will remain unchanged.

### 1.2 Ask to your ISP a DNS

Some internet provider offer a DNS service that can be used for your web application. A DNS (Domain Name Service) resolves your router ip to a specific name. `Free`  provides this option and you can choose a name for your server (if it is not already in use). Go into the `MAFREEBOX > Personnaliser mon reverse DNS` then at the bottom of the page, enter a name for your server in the field `Reverse DNS personnalisé`. For instance my server name is `xxxxxx.hd.freebox.fr`. 

### 1.3 Use Nginx server as reverse proxy

[Nginx](https://www.nginx.com/) server is another web server. Compared to `Flask`, `Nginx` is production oriented server. However, `Flask` is very practical for prototyping and hobbies. Using `Nginx` as a reverse proxy allow to dedicate the SSL security to `Nginx` while keeping the content under the hood of `Flask` server. Below is a small diagram that explain what's happening when you try to reach the server:

![Image Stream Server Image](https://github.com/bcrobo/image_stream_server/blob/main/doc/img/image_stream_server.png)

You can easily install `Nginx` using `sudo apt-get install nginx`. Once this is done, you should configure `Nginx` to act as a proxy.
This will be describe in section 5.

### 1.4 Ask a SSL certificate from LetsEncrypt entity (remote access only)

[LetsEncrypt](https://letsencrypt.org/) is a nonprofit certificate authority. You can ask for a certificate using their utility program `certbot`. Its installation is very simple `sudo apt-get install certbot`.

To ask a certificate you can use the following command line:

`sudo letsencrypt certonly --dry-run --manual --email youremailaddress@xxxxx.com -d xxxxxxx.hd.free.fr`

It will prompt you a message asking to your server to reply a specific hash when a specific URL is queried by `LetsEncrypt`. By doing so, `LetsEncrypt` so they ensure you are the owner of the server. For doing this we will modify our `Flash` application to answer that hash.
Once this is done, you should have a certificate, and a private key in the `/etc/letsencrypt/live/your-dns-name` directory.

**NOTE**: This operation can also be performed at the `Nginx` level.

The modification looks like:
```
@auth.route('/.well-known/acme-challenge/<challenge>')
def letsencrypt_check(challenge):
    challenge_response = {
       "SyVlwQEXFZDlHUzT28Ko6azone2j2hRuROOT5jlDDk0":"SyVlwQEXFZDlHUzT28Ko6azone2j2hRuROOT5jlDDk0.CsnZA_XCWM39H5F1SjCSbq5yGPswgizWR5WLnn6aoUQ",
    }
    return Response(challenge_response[challenge], mimetype='text/plain')
```
The certificate is usually valid for a period of 90 days but it can be easily renewed.

### 1.5 Configuration of Nginx

Now, we'll indicate `Nginx` to listen on the `443` port (https) and to redirect all `80` port traffic to the `443` port to be sure that the connection to your server will be secure using the `https` protocol. Furthermore we will give him the path to certificate file and private key to use to encrypt the connection.
You can create a `Nginx` configuration file in `/etc/nginx/conf.d` directory and link that file into the `/etc/nginx/site-enabled` and directories.
The configuration file typically look like this:

```
server {
  listen 443 ssl;
  server_name your-dns-name www.your-dns-name;
  ssl_certificate /etc/letsencrypt/live/your-dns-name/cert.pem;
  ssl_certificate_key /etc/letsencrypt/live/your-dns-name/privkey.pem;
  location / {
    proxy_pass http://127.0.0.1:5000/;
    #proxy_set_header Host $host;
    #proxy_set_header X-Real-IP $remote_addr;
    #proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    #proxy_set_header X-Forwarded-Proto $scheme;
  }
}

server {
    listen 80;
    server_name your-dns-name www.your-dns-name;
    location / {
        return 301 https://$host$request_uri;
    }
}

```

Your server is now ready to receive incoming connections.

### 1.6 Router port redirection

The last step is to open the `443` (https) port for `TCP` traffic on your router and redirect the traffic to the machine that host your server in your local network. These redirections can be defined using the web interface of your router `mafreebox.freebox.fr` for my ISP for instance. The machine that host my server is my raspberry pi. In `Paramètre de la freebox > Gestion des ports` I added two rules, that redirect all incoming traffic of port `80` and `443` to my raspberry pi ip. The image below shows the rule I added:

![Port Redirection](https://github.com/bcrobo/image_stream_server/blob/main/doc/img/port_redirection.png)

Once enable, you should be able to reach your server from the world wide web.



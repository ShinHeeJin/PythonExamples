## MailHog on Docker

start mailhog from from dockerhub

```docker
docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog
```

mount mailhog maildirectory to local filysystem

```docker
docker run -d -e "MH_STORAGE=maildir" -v $PWD/maildir:/maildir -p 1025:1025 -p 8025:8025 mailhog/mailhog
```

mailhog on Docker Compose

```yaml
version: "3"
services:
  mailhog:
    image: mailhog/mailhog
    ports:
      - "11025:1025"
      - "18025:8025"
```

```bash
docker-compose up -d mailhog
```

default setting
- the SMTP server starts on port 1025
- the HTTP server starts on port 8025
- in-memory message storage


refrence
https://kinsta.com/blog/mailhog/#mailhog-on-docker
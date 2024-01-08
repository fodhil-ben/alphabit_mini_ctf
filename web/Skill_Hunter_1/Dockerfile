FROM php:8.2-apache

RUN apt-get update

COPY src/ /var/www/html/
COPY flag.txt /
RUN useradd -m myuser
USER myuser
WORKDIR /var/www/html/


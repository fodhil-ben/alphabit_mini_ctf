FROM php:8.2-apache

RUN apt-get update
RUN docker-php-ext-install exif

COPY src/ /var/www/html/
COPY see_FLAG.png /
COPY hint.txt /
RUN useradd -m myuser
USER myuser
WORKDIR /var/www/html/
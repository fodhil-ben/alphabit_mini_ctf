FROM php:8.2-apache

RUN apt-get update
RUN docker-php-ext-install exif

COPY src/ /var/www/html/
COPY see_FLAG.png /


WORKDIR /var/www/html/
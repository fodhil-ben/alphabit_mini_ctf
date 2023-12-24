#!/bin/sh

docker build -t sqli .

docker run -p 1337:1337 sqli

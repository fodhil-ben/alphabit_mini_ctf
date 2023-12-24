#!/bin/sh

docker build -t templates .

docker run -p 1332:1332 templates

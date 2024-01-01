#!/bin/sh

docker build -t format .

docker run -p 1232:1232 format

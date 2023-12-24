#!/bin/sh

docker build -t forgery .

docker run -d -p 1335:1335 forgery

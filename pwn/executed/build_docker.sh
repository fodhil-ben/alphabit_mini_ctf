#!/bin/sh

docker build -t executed .

docker run -p 1233:1233 executed

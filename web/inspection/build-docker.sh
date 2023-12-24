#!/bin/sh

docker build -t inspection .

docker run -p 1333:1333 inspection
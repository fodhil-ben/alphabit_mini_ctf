#!/bin/sh

docker build -t headers_hunter .

docker run -p 1336:1336 headers_hunter
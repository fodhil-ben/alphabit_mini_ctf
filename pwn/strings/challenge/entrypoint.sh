#!/bin/sh
EXEC="./strings"
PORT=1004

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive EXEC:"$EXEC",stderr
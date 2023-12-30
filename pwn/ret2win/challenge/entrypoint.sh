#!/bin/sh
EXEC="./chal "
PORT=1003

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive EXEC:"$EXEC",stderr
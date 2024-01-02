#!/bin/sh
EXEC="./chall"
PORT=1010

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive EXEC:"$EXEC",stderr
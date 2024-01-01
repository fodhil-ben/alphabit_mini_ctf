#!/bin/sh
EXEC="./chal"
PORT=1008

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive EXEC:"$EXEC",stderr
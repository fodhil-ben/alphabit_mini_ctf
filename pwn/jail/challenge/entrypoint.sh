#!/bin/sh
EXEC="./chal"
PORT=1009

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive EXEC:"$EXEC",stderr
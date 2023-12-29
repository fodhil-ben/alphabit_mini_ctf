#!/bin/sh
EXEC="./deadcode"
PORT=1001

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive EXEC:"$EXEC",stderr
#!/bin/sh
EXEC="./can"
PORT=4001

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive EXEC:"$EXEC",stderr
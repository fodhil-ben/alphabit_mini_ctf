#!/bin/sh
EXEC="./secret_number_game"
PORT=1000

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive EXEC:"$EXEC",stderr
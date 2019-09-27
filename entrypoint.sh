#!/bin/sh

python3 /src/app.py &

exec nginx -g 'daemon off;'

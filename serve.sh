#!/bin/bash

# check input arguments
if [[ $# -lt 1 ]]; then
    echo "USAGE: $0 spec.json"
    exit 1
fi

# location of vega-sandbox directory
VEGA_SANDBOX=$(cd "$(dirname "$0")" ; pwd)

# get an open port
PORT=$(python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')

# kick off flask server
SPEC=$1 FLASK_APP=${VEGA_SANDBOX}/flask_server.py flask run -p $PORT &

# open in web browser
sleep 1
if [[ $(uname) == Darwin ]]; then
    open "http://localhost:$PORT"
else
    xdg-open "http://localhost:$PORT"
fi

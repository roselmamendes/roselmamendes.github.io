#!/bin/bash

case "$1" in
'build-layout')
echo "Building the blog"
docker run --rm -v "$PWD":/usr/src/app -it roselma-pelican pelican
;;

'build-layout-watch')
echo "Building the blog"
sudo docker run --rm -v "$PWD":/usr/src/app -it roselma-pelican pelican -r
;;

'start-server')
echo "Starting server"
sudo docker run --rm -v "$PWD/docs":/usr/src/app -p 8000:8000 -it roselma-pelican python -m http.server --bind 0.0.0.0
;;

'build-docker-image')
echo "Building the project"
sudo docker build -t roselma-pelican .
;;

esac
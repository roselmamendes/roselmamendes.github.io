# Contributing

## Requirements for local development

- Docker

## Run locally

1. Git clone this repository
2. On the repository folder, build the docker image with `sh cli/blog.sh build-docker-image`
3. Start the server with `sh cli/blog.sh start-server`

To build the static content run `sh cli/blog.sh build-layout`.

## Deploy

With Github Pages, `git push` the folder /blog and configure the repository to use the folder /blog to publish the blog.

To publish in Github Pages, run `sh cli/blog.sh publicar`. It will use the pelican' publishconf to build the folder blog.
Title: A blog with Pelican
Date: 2019-01-10 10:20
Modified: 2019-01-10 10:20
Category: Python
Tags: pelican, publishing
Slug: tec/static-sites-pelican
Authors: Roselma Mendes
Summary: Having a web site usigin Pelican
Image: pelican.jpg
Status: draft

## Pelican

What is it

## Preparing the local environment

I am using Docker. So first I created a Dockerfile as following:

    :::docker
    FROM python:latest
    
    WORKDIR /usr/src/app
    
    COPY requirements.txt ./
    RUN pip install --no-cache-dir -r requirements.txt
    
    COPY . .
    
    EXPOSE 8000
    
**How I organized the folder**

I highlighted only the folders and files mentioned on this post. I may miss others from pelican-quickstart command.

```
blog-root
--theme
    -static
    -templates
--content
    - pages
--pelicanconf.py
--publishconf.py
--Dockerfile
--requirements.txt
```
    
## Preparing Pelican

start the project with pelican-quickstart
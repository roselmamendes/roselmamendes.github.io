#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'roselmamendes'
SITENAME = 'Blog da Roselma Mendes'
SITEURL = ''

HEADER_COVER = 'images/capa3.jpeg'
AUTHORS_BIO = {
  "roselmamendes": {
    "name": "Roselma Mendes",
    "image": "images/roselma_.jpg",
    "website": "http://roselmamendes.github.io/blog",
    "twitter": "roselmamendes",
    "github": "roselmamendes",
    "location": "Recife/Brasil",
    "bio": "Feminista Negra Interseccional que ama programação e trabalha na área desde 2010. Baiana. Uma ThoughtWorker. Curte programação fullstack. Se interessa por Arquitetura de Sistemas: Entrega de Software, infra, design de aplicações, segurança, e por ai vai."
  }
}

PATH = 'content'
OUTPUT_PATH = 'blog'
TIMEZONE = 'America/Recife'

DEFAULT_LANG = 'pt-br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/roselmamendes'),
          ('github', 'https://github.com/roselmamendes'),
          ('envelope','mailto:roselma.mendes@gmail.com'))

DEFAULT_PAGINATION = 5

THEME='attila-1.3'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
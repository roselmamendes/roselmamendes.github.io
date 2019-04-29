#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Roselma Mendes'
SITENAME = 'Blog da Roselma Mendes'
SITEURL = ''

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
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/roselmamendes'),
          ('github', 'https://github.com/roselmamendes'),)

DEFAULT_PAGINATION = 5

#OUTPUT_PATH = 'server/templates'

THEME = "./theme"

SITELOGO = SITEURL + 'theme/img/IMG_2576.jpg'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TEMPLATE_PAGES = {'outros-textos.html': 'outros-textos.html',
'404.html': '404.html'
}
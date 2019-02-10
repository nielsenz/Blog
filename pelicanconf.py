#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Zach Nielsen'
SITEURL = ''
SITENAME = u"Zach Nielsen's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = 'Data Driven Analyst | Transforming Numbers into Stories'
EMAIL = 'zach@zachnielsen.org'
RESPONSIVE_IMAGES = True
SINGLE_AUTHOR = True
COPYRIGHT_YEAR = 2018

SITELOGO = '../images/logo.png'


PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
  #       ('Python.org', 'http://python.org/'),
  #       ('Jinja2', 'http://jinja.pocoo.org/'),
   #      ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/nielsenz'),
          ('twitter', 'https://twitter.com/Niels506'),
          ('github', 'https://github.com/nielsenz'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

##Will plugins ever work? I'll keep you posted/
PLUGIN_PATHS = ['./plugins']
#PLUGINS = ['neighbors']

THEME ="pelican-themes/Flex"	#Theme number 3. It works with Google Analytics!
TYPOGRIFY = True
STATIC_PATHS = ['images', 'pdfs']

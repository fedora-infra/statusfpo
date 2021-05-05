# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fedora Infrastructure Team'
SITENAME = 'Fedora Infrastructure Status'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = []
THEME = 'theme'

USE_FOLDER_AS_CATEGORY = True

AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

#Use basename(filename) rather than title for slugs 
SLUGIFY_SOURCE = 'basename'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = 'feeds/{slug}.rss'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['plugins']
PLUGINS = ['filters', 'pelicanversion']


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DIRECT_TEMPLATES = (('index', 'resolved'))

# Some specific settings just for status.fp.o

TICKET_TRACKER_URL = 'https://pagure.io/fedora-infrastructure/issue/'

# Minimum Pelican Version -- used by our custom pelicanversion plugin
MIN_PELICAN_VERSION = '4.5.4'
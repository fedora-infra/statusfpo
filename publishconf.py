# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://status.fedoraproject.org'
RELATIVE_URLS = False

FEED_ALL_RSS = 'changes.rss'
CATEGORY_FEED_RSS = '{slug}.rss'

DELETE_OUTPUT_DIRECTORY = True
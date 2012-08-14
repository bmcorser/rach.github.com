#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
import sys
sys.path.append(os.getcwd())

ROOT = os.path.realpath(os.getcwd())
THEME = os.path.join(ROOT,'theme')
#THEME = 'notmyidea'
AUTHOR = u"Rach Belaid"
SITETITLE= u"Rach Belaid's blog"
SITENAME = u"There's a snake in my boot!"
SITESUBTITLE = u"Python Charmer, Git Lover, OpenSource Admirer, Technology Dreamer"
SITEURL = 'http://rachbelaid.com'
RELATIVE_URLS = False
PAGE_DIR='pages'

TIMEZONE = 'Europe/London'
GITHUB_REPO = "https://github.com/rach/rach.github.com"
GIT_BRANCH = 'source'
GITHUB_EDIT_PREFIX = "%s/blob/%s" % (GITHUB_REPO, GIT_BRANCH)
TWITTER_USERNAME = 'rachbelaid'
TWITTER_SHARE_URL_SCHEMA = "https://twitter.com/intent/tweet?original_referer=%s&related=%s&via=%s&text=%s&url=%s"
TWITTER_SHARE_URL = TWITTER_SHARE_URL_SCHEMA % (SITEURL, TWITTER_USERNAME, TWITTER_USERNAME, "%s", "%s")
DEFAULT_LANG='en'
#GOOGLE_ANALYTICS = ""
# Social widgets
# Name , link, new page
SOCIAL =  (

     ('Me', '%s/about-me.html'% SITEURL , False  ),
     ('Twitter', 'https://twitter.com/rachbelaid', True),
    ('Linkedin', 'http://uk.linkedin.com/in/rachbelaid', True),
    ('Github', 'http://github.com/rach/', True),
         )

# Links
LINKS = (

         )

DEFAULT_PAGINATION = 7
DEFAULT_ORPHANS = 1

DISQUS_SITENAME = "rach-belaid-blog"

DEFAULT_DATE_FORMAT = "%d %b %Y"
# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),('extra/CNAME', 'CNAME'),)

#STATIC_PAGES = {'/me.html': 'static/me.html', }

#PLUGIN_PATH = "plugins"
#from plugins.bitly import bitly_plugin
#PLUGINS = [bitly_plugin,]


#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
ROOT = os.path.realpath(os.getcwd())
THEME = os.path.join(ROOT,'themes','rach')
#THEME = 'notmyidea'
AUTHOR = u"Rach Belaid"
SITETITLE= u"Rach Belaid's blog"
SITENAME = u"There's a snake in my boot!"
SITESUBTITLE = u"Python Charmer, Git Lover, OpenSource Admirer, Technology Dreamer"
SITEURL = '/'

TIMEZONE = 'Europe/London'
GITHUB_REPO = "https://github.com/rach/rach.github.com"
GIT_BRANCH = 'source'
GITHUB_EDIT_PREFIX = "%s/blob/%s" % (GITHUB_REPO, GIT_BRANCH)

DEFAULT_LANG='en'

# Blogroll
LINKS =  (
    ('Twitter', 'https://twitter.com/rachbelaid'),
    ('Linkedin', 'http://uk.linkedin.com/in/rachbelaid'),
    ('Github', 'http://github.com/rach/'),
         )

# Social widget
SOCIAL = (
          ('You can add links in your config file', '#'),
         )

DEFAULT_PAGINATION = 7
#PLUGIN_PATH = "plugins"
import os
import sys
sys.path.append(os.getcwd())
DEFAULT_DATE_FORMAT = "%d %b %Y"
#import pdb; pdb.set_trace()
from plugins.bitly import bitly_plugin
PLUGINS = [bitly_plugin,]


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




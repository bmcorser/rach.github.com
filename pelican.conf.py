#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
ROOT = os.path.realpath(os.getcwd())

THEME = os.path.join(ROOT,'themes','rach')
#THEME = 'notmyidea'
AUTHOR = u"Rach Belaid"
SITETITLE= u"Rach Belaid's blog"
SITENAME = u"There's a snake in my boot!"
SITESUBTITLE = u"Python Charmer, Git Lover, OpenSource Idolizer, Technology dreamer"
SITEURL = '/'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG='en'

# Blogroll
LINKS =  (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
    ('Jinja2', 'http://jinja.pocoo.org'),
    ('You can modify those links in your config file', '#')
         )

# Social widget
SOCIAL = (
          ('You can add links in your config file', '#'),
         )

DEFAULT_PAGINATION = 7




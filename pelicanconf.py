#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Clayton Blythe'
SITENAME = 'Deep Python'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME="/users/claytonblythe/Desktop/Mega/Data_Science/projects/pelican-themes/elegant"


LANDING_PAGE_ABOUT = {'title': 'Deep Python:  Using Python for Deep Learning',
        'details': """<div itemscope itemtype="http://schema.org/Person"><p>My name
        is <span itemprop="name">Clayton Blythe</span>.<p>I work at Ford Motor Company <a href="http://ford.com/"
        title="Ford Motor Company" itemprop="affiliation">Ford Motor Company</a> as a Machine Learning / Artificial Intelligence scientist. I play a broad role there, which
        includes research, product development, engineering and deployment for a variety of data intensive projects such as cybersecurity, customer interaction,
        and autonomous vehicle detection initiatives.
        </p>You can find my github profile at <a href="https://github.com/claytonblythe/" title="My Github
       profile" itemprop="url"><span itemprop="nickname">github.com/claytonblythe</span></a>  You can also reach me
       via my personal email at <a
       href="mailto:claytondblythe@gmail.com" title="My email
       address" itemprop="email">claytondblythe@gmail.com</a>.</p><p>I mostly work in Python, OSX and Linux, I also occasionally dabble in other languages like R, Scala, and Go. </p><p>Besides programming, I like to exercise, go to
       live concerts, tinker with my raspberry pi, drink beer, and play guitar.
       </p></div>"""}

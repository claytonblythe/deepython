#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Clayton Blythe'
SITENAME = u""" <span style="color:#254601;">deepython.com | Clayton Blythe </span>"""
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
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('LinkedIn', 'http://linkedin.com/in/claytonblythe'),
          ('Github', 'http://github.com/claytonblythe'),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME="/users/claytonblythe/Desktop/Mega/Data_Science/projects/pelican-themes/elegant"


LANDING_PAGE_ABOUT = {'title': 'Deep Python:  Using Python for Deep Learning',
        'details': """<div itemscope itemtype="http://schema.org/Person"><p>My name
        is <span itemprop="name">Clayton Blythe</span>.<p>I work at <a href="http://ford.com/"
        title="Ford Motor Company" itemprop="affiliation">Ford Motor Company</a> as a Machine Learning / Artificial Intelligence scientist. I play a broad role there, which
        includes research, product development, engineering and deployment for a variety of data intensive projects such as cybersecurity, customer interaction,
        and autonomous vehicle detection initiatives.
        </p>You can take a look at my <a href="https://github.com/claytonblythe/" title="My Github
       profile" itemprop="url"><span itemprop="nickname">Github profile</span></a>, reach out to me
       at my personal email <a
       href="mailto:claytondblythe@gmail.com" title="My email
       address" itemprop="email">claytondblythe@gmail.com</a>, or mesage me on <a
       href="http://linkedin.com/in/claytonblythe" title="My linkedin
       profile" itemprop="linkedin">LinkedIn.</a></p><p>I mostly work in Python within OSX and Linux, but I have also occasionally dabbled in other languages like R, Scala, and Go. </p><p>Besides programming, I like to exercise, go to
       live concerts, tinker with my raspberry pi testingtesting projects, drink beer, and play guitar.
       </p></div>"""}

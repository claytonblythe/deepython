#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Clayton Blythe'
SITENAME = u""" <span style="color:#254601;">deepython.com | Clayton Blythe </span>"""
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

# Appearance
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}.html'
PAGE_URL = u'{slug}.html'
PAGE_SAVE_AS = u'{slug}.html'

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


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME='/users/claytonblythe/Desktop/Mega/Data_Science/projects/elegantdp'

LANDING_PAGE_ABOUT = {'title': 'Deep Python:  Using Python for Deep Learning',
        'details': """<div itemscope itemtype="http://schema.org/Person"><p>My name
        is <span itemprop="name">Clayton Blythe</span>.<p>I am a 22 year old guy working for <a href="http://ford.com/"
        title="Ford Motor Company" itemprop="affiliation">Ford Motor Company</a> as a Machine Learning / Artificial Intelligence Scientist. I play a broad role there, which
        includes research, product development, engineering and deployment for a variety of data intensive projects such as cybersecurity, customer interaction,
        and autonomous vehicle detection initiatives.
        </p>You can take a look at my <a href="https://github.com/claytonblythe/" title="Github
       profile" itemprop="url"><span itemprop="nickname">Github profile</span></a>, reach out to me
       at my personal email <a
       href="mailto:claytondblythe@gmail.com" title="personal email
       " itemprop="email">claytondblythe@gmail.com</a>, or mesage me on <a
       href="http://linkedin.com/in/claytonblythe" title="LinkedIn
       profile" itemprop="linkedin">LinkedIn.</a> You can also download my <a
       href="http://deepython.com.s3-website.us-east-2.amazonaws.com/august_resume.pdf" title="My resume" itemprop="resume">resume</a> here if you want. </p>
       <p>I mostly work in Python within OSX and Linux, but I have also occasionally dabbled in other languages like R, Scala, and Go. </p><p>Besides programming, I like to exercise, go to
       live concerts, tinker with my raspberry pi, drink beer, and play guitar.
       </p></div>"""}


# Legal
SITE_LICENSE = u'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">deepython.com</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://deepython.com" property="cc:attributionName" rel="cc:attributionURL">Clayton Blythe</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'


# Landing Page
PROJECTS = [
        {
            'name': 'Movie Colorify',
            'url':
            'https://github.com/claytonblythe/movie_colorify',
            'description': 'A visual color palatte representation of any movie, written in Python'},
        {
            'name': 'Wifi Speed Tracking',
            'url':
            'https://github.com/claytonblythe/wifi_speed_tracking',
            'description': 'A wifi speed-logging program'},
        {
            'name': 'Computational Nanoscience',
            'url':
            'https://github.com/claytonblythe/spectral_analysis',
            'description': 'Analyzing circularly polarized high harmonic generation in helium'},
        {
            'name': 'Historical S&P 500 Performance Analysis ',
            'url':
            'https://github.com/claytonblythe/S-P500_outcomes',
            'description': 'An investigation into historical returns of the S&P 500'},
        {
            'name': 'Reddit Image Downloader',
            'url': 'https://github.com/claytonblythe/subredditTopImagesDownloader',
            'description': 'Command-line program to download popular images from a subreddit'},
        {
            'name': 'Craft Beer Analysis',
            'url':
            'https://github.com/claytonblythe/beer_advocate_reccommender',
            'description': 'Which breweries have the best beer?'}]

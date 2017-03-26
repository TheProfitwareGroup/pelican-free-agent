#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from imp import load_source
sigal_conf = load_source('sigal_conf', 'sigal.conf.py')

AUTHOR = sigal_conf.author
SITENAME = sigal_conf.sitename
SITESUBTITLE = sigal_conf.subtitle

SITEURL = '.'


THEME_STATIC_DIR = 'static'
PATH = 'content'
STATIC_PATHS = [ 'images','mail','js', 'css', 'fonts']
EXTRA_PATH_METADATA = {
    'static/images/portfolio': {'path': 'images/portfolio'},
    }
TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru'
BOOTSTRAP_FILE = 'bootstrap.min.css'
CSS_FILE = 'freeagent.css'
FONTS = 'fonts'
SCRIPTS = [
	'jquery-1.11.0.js',
	'bootstrap.min.js',
	'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js',
	'classie.js',
	'cbpAnimatedHeader.js',
	'jqBootstrapValidation.js',
	'contact_me.js',
	'freeagent.js'
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DIRECT_TEMPLATES = ['index']

# Top Menu Links
NAVLINKS = (
	('#page-top', ''),
	('#portfolio', 'Portfolio'),
	('#about', 'About'),
	('#contact', 'Contact')
)

# Portfolio Name
PORTFOLIO = sigal_conf.portfolio



#Contact form fields sorted by: label, input_type, id, required_validation_,msg
CONTACT_FIELDS = (
	['Name', 'text', 'name', 'Please enter your name.'],
	['Email Address', 'email', 'email','Please enter your email address.' ],
	['Phone Number', 'tel', 'phone', 'Please enter your phone number.'],
	['Message', 'textarea', 'message', 'Please enter a message.']
)
EMAIL = sigal_conf.email

ADDRESS1 = 'The Internet'
ADDRESS2 = 'Moscow, Russia'
# Left column
ABOUT_LEFT = 'Something on the left'
# Right column
ABOUT_RIGHT = 'Something on the right'
# Center
ABOUT_CENTER = '<a href="https://github.com/TheProfitwareGroup" target="_blank" class="btn btn-lg btn-outline"><i class="fa fa-download"></i>&nbsp;Visit our Github</a>'

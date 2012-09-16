#!/usr/bin/env python
from sploitego.config import config
from facebook import GraphAPI, get_app_access_token

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Sploitego Project'
__credits__ = ['Nadeem Douba']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'


def login():
    return GraphAPI(
        config['facebook/access_token']
    )
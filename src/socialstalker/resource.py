#!/usr/bin/env python


from pkg_resources import resource_filename
from os import path

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Sploitego Project'
__credits__ = ['Nadeem Douba']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'


def imageicon(name):
    return 'file://%s' % path.abspath(resource_filename('socialstalker.resources.images', name))


#!/usr/bin/env python

from sploitego.framework import configure
from sploitego.maltego.message import Phrase
from socialstalker.transforms.common.entities import FacebookLike

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Sploitego Project'
__credits__ = ['Nadeem Douba']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'


@configure(
    label='To Category [FB]',
    description='Returns the category of the Facebook like.',
    uuids=['socialstalker.v2.FacebookLikeToCategory_FB'],
    inputs=[( "Social Media", FacebookLike )]
)
def dotransform(request, response):
    response += Phrase(request.fields['category'])
    return response

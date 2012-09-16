#!/usr/bin/env python

from sploitego.framework import configure
from facebook import GraphAPIError
from sploitego.maltego.message import AffiliationFacebook, UIMessage
from unicodedata import normalize
from common.entities import FacebookLike
from socialstalker.resource import imageicon
from common.facebookutils import login

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, SocialStalker Project'
__credits__ = ['Nadeem Douba']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'


def getlikes(response, data):

    for like in data:
        like['name'] = normalize('NFKD', like['name']).encode('ascii', 'ignore')
        e = FacebookLike(like['name'])
        e.fromname = like['name']
        e.id = like['id']
        e.category = like['category']
        e.iconurl = imageicon('fblike.gif')
        response += e


@configure(
    label='To Facebook Likes [FB]',
    description='Finds out what the user likes on Facebook.',
    uuids=['socialstalker.v2.AffiliationFacebookToLikes_FB'],
    inputs=[( "Social Media", AffiliationFacebook )]
)
def dotransform(request, response):

    graph = login()

    try:
        b = f = graph.request('%s/likes' % request.fields['uid'])

        while graph.has_next(f):
            getlikes(response, f['data'])
            f = graph.next(f)

        while graph.has_previous(b):
            b = graph.previous(b)
            getlikes(response, b['data'])

    except GraphAPIError, e:
        response += UIMessage(str(e))

    return response
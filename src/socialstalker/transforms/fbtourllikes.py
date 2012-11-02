#!/usr/bin/env python

from canari.framework import configure
from facebook import GraphAPIError
from canari.maltego.message import UIMessage, Field
from canari.maltego.entities import AffiliationFacebook, URL
from common.facebookutils import login

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, SocialStalker Project'
__credits__ = ['Nadeem Douba']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'


@configure(
    label='To URL Likes [FB]',
    description='Finds out what URLs the user likes on Facebook.',
    uuids=['socialstalker.v2.AffiliationFacebookToUrls_FB'],
    inputs=[( "Social Media", AffiliationFacebook )]
)
def dotransform(request, response):

    graph = login()

    try:
        r = graph.fql('SELECT url FROM url_like WHERE user_id = %s' % request.fields['uid'])
        for u in r:
            e = URL('%s ...' % (u['url'][:50] if len(u['url']) > 50 else u['url']))
            e += Field('url', u['url'])
            response += e

    except GraphAPIError, e:
        response += UIMessage(str(e))

    return response
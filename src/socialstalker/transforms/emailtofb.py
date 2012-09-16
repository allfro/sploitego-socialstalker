#!/usr/bin/env python

from facebook import GraphAPIError
from sploitego.framework import configure
from sploitego.maltego.message import EmailAddress, AffiliationFacebook, UIMessage
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
    label='To Facebook Affiliation [FB]',
    description='Finds a Facebook user based on their email address.',
    uuids=[ 'socialstalker.v2.EmailToFacebookAffiliation_FB' ],
    inputs=[ ( "Social Media", EmailAddress ) ]
)
def dotransform(request, response):

    graph = login()

    try:
        r = graph.request('search', {'q' : request.value, 'type' : 'user'})

        if r['data']:
            u = r['data'][0]
            e = AffiliationFacebook(u['name'])
            e.uid = u['id']
            e.profileurl = 'https://www.facebook.com/%s' % u['id']
            response += e
    except GraphAPIError, e:
        response += UIMessage(str(e))


    return response

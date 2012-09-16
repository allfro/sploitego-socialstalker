#!/usr/bin/env python

from facebook import GraphAPIError
from sploitego.framework import configure
from sploitego.maltego.message import Person, AffiliationFacebook, UIMessage
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
    label='To Facebook Username [FB]',
    description='Finds a Facebook username based on their UID.',
    uuids=[ 'socialstalker.v2.FacebookAffiliationToUsername_FB' ],
    inputs=[ ( "Social Media", AffiliationFacebook ) ]
)
def dotransform(request, response):

    graph = login()

    try:
        r = graph.request(request.fields['uid'])

        if 'username' in r:
            response += Person(r['username'])
    except GraphAPIError, e:
        response += UIMessage(str(e))

    return response

#!/usr/bin/env python

from sploitego.framework import configure
from sploitego.maltego.message import EmailAddress
from socialstalker.transforms.common.entities import AffiliationFoursquare
from socialstalker.transforms.common.foursquareutils import login


__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Sploitego Project'
__credits__ = ['Nadeem Douba']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'


@configure(
    label='To Foursquare [FS]',
    description='Gets Foursquare user profile from email address.',
    uuids=['socialstalker.v2.EmailToFoursquare_FS'],
    inputs=[( "Social Media", EmailAddress )]
)
def dotransform(request, response):

    client = login()

    user = client.users.search({'email' : request.value})['results']

    for u in user:
        e = AffiliationFoursquare('%s %s' % (u['firstName'], u.get('lastName', '')))
        e.uid = u['id']
        e.network = 'Foursquare'
        e.profileurl = 'https://foursquare.com/user/%s' % u['id']
        response += e

    return response

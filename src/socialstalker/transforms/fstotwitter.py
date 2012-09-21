#!/usr/bin/env python

from sploitego.framework import configure
from sploitego.maltego.message import PhoneNumber, AffiliationTwitter
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
    label='To Twitter [FS]',
    description='Gets Twitter user profile from Foursquare contact info.',
    uuids=['socialstalker.v2.FoursquareToTwitter_FS'],
    inputs=[( "Social Media", AffiliationFoursquare )]
)
def dotransform(request, response):

    client = login()

    user = client.users(request.fields['affiliation.uid']).get('user', {})

    if 'contact' in user and 'twitter' in user['contact']:
        e = AffiliationTwitter(user['contact']['twitter'])
        e.profileurl = 'http://twitter.com/%s' % user['contact']['twitter']
        e.network = 'Twitter'
        e.uid = user['contact']['twitter']
        response += e

    return response

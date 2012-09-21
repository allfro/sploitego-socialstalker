#!/usr/bin/env python
import re

from sploitego.framework import configure
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
    label='To Foursquare Friends [FS]',
    description='Gets user Foursquare friends.',
    uuids=['socialstalker.v2.FoursquareToFoursquareFriends_FS'],
    inputs=[( "Social Media", AffiliationFoursquare )]
)
def dotransform(request, response):

    client = login()

    for f in client.users.friends(request.fields['affiliation.uid'])['friends']['items']:
        if 'type' not in f:
            e = AffiliationFoursquare('%s %s' % (f['firstName'], f.get('lastName', '')))
            e.profileurl = 'https://foursquare.com/user/%s' % f['id']
            e.network = 'Foursquare'
            e.uid = f['id']
            response += e

    return response

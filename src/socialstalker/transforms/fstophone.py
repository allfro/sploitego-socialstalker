#!/usr/bin/env python

from sploitego.framework import configure
from sploitego.maltego.message import PhoneNumber
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
    label='To Phone Number [FS]',
    description='Gets user phone number from Foursquare contact info.',
    uuids=['socialstalker.v2.FoursquareToPhoneNumber_FS'],
    inputs=[( "Social Media", AffiliationFoursquare )]
)
def dotransform(request, response):

    client = login()

    user = client.users(request.fields['affiliation.uid']).get('user', {})

    if 'contact' in user and 'phone' in user['contact']:
        e = PhoneNumber(user['contact']['phone'])
        response += e

    return response

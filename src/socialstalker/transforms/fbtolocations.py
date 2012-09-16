#!/usr/bin/env python

from sploitego.framework import configure
from facebook import GraphAPIError
from sploitego.maltego.message import AffiliationFacebook, UIMessage, Location, Field
from common.facebookutils import login

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, SocialStalker Project'
__credits__ = ['Nadeem Douba']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'


def getlocs(response, data):

    for loc in data:
        l = loc['place']['location']
        e = Location('%s, %s' % (l.get('city', ''), l.get('country', '')))
        if  'country' in l:
            e.country = l['country']
        if 'city' in l:
            e.city = l['city']
        if 'state' in l:
            e.area = l['state']
        if 'longitude' in l and 'latitude' in l:
            e.longitude = l['longitude']
            e.latitude = l['latitude']
        sa = ''
        if 'name' in loc['place']:
            sa = loc['place']['name']
        if 'street' in l:
            sa += ', %s' % l['street']
        if 'zip' in l:
            sa += ', %s' % l['zip']
        e += Field('streetaddress', sa)
        response += e


@configure(
    label='To Locations [FB]',
    description='Finds out where the user was via Facebook.',
    uuids=['socialstalker.v2.AffiliationFacebookToLocations_FB'],
    inputs=[( "Social Media", AffiliationFacebook )]
)
def dotransform(request, response):

    graph = login()

    try:
        b = f = graph.request('%s/locations' % request.fields['uid'])

        while graph.has_next(f):
            getlocs(response, f['data'])
            f = graph.next(f)

        while graph.has_previous(b):
            b = graph.previous(b)
            getlocs(response, b['data'])

    except GraphAPIError, e:
        response += UIMessage(str(e))

    return response
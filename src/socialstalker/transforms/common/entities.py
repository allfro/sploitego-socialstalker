#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField
from canari.maltego.entities import Affiliation

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, SocialStalker Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'

__all__ = [
    'SocialStalkerEntity'
]


class SocialStalkerEntity(Entity):
    namespace = 'socialstalker'


@EntityField(name="category")
@EntityField(name="from.id", propname="id", displayname="ID")
@EntityField(name="from.name", propname="fromname", displayname="Name")
@EntityField(name="url", displayname="URL")
class FacebookLike(SocialStalkerEntity):
    pass


class PacketNinjasEntity(Affiliation):
    namespace = 'packetninjas'


class AffiliationFoursquare(PacketNinjasEntity):
    name = 'affiliation.Foursquare'


@EntityField(name="rank")
@EntityField(name="displayname", propname="displayname", displayname="Display Name")
class AffiliationSkype(SocialStalkerEntity):
    name = 'affiliation.Skype'


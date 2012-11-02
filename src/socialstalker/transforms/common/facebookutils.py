#!/usr/bin/env python

from posix import unlink

from canari.easygui import multenterbox
from os import path
from canari.utils.fs import cookie, fmutex
from facebook import GraphAPIError, GraphAPI

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Sploitego Project'
__credits__ = ['Inspired by http://blog.carduner.net/2010/05/26/authenticating-with-facebook-on-the-command-line-using-python/']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'


def login():

    client = None

    if not path.exists(cookie('facebook')):

        for i in range(0, 3):
            token = multenterbox("Enter a valid Facebook access token", ['Access Token'], [''])[0]
            try:
                client = GraphAPI(token)
                client.request('me')
                fmutex('facebook').write(token)
                return client
            except GraphAPIError, e:
                print str(e)
                pass

        raise GraphAPIError('Unable to query GraphAPI')

    try:
        client = GraphAPI(file(cookie('facebook')).read())
        client.request('me')
    except GraphAPIError, e:
        unlink(cookie('facebook'))
        return login()
    return client


#access_token = None
#
#class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
#
#    def do_GET(self):
#        global access_token
#        self.send_response(200)
#        self.send_header("Content-type", "text/html")
#        self.end_headers()
#
#        if '/?code=' not in self.path:
#            return
#        code = parse_qs(urlparse(self.path).query).get('code')
#        code = code[0] if code else None
#        debug('Code is %s' % code)
#
#        if code is None:
#            self.wfile.write("Sorry, authentication failed.")
#            access_token =  ''
#            return
#
#        response = get_access_token_from_code(
#            code,
#            config['facebook/redirect_uri'],
#            config['facebook/app_id'],
#            config['facebook/app_secret']
#        )
#
#        access_token = response['access_token']
#
#        fmutex('facebook').write(access_token)
#
#        self.wfile.write("You have successfully logged in to facebook. "
#                         "You can close this window now.")
#
#
#def login():
#    global access_token
#    if not path.exists(cookie('facebook')):
#        debug("Logging you in to facebook...")
#        webbrowser.open(auth_url(
#            config['facebook/app_id'],
#            config['facebook/redirect_uri'],
#            perms=config['facebook/permissions']
#        ))
#
#        listen_on = urlsplit(config['facebook/redirect_uri'])
#        httpd = BaseHTTPServer.HTTPServer((listen_on.hostname,listen_on.port or 80), RequestHandler)
#        while access_token is None:
#            httpd.handle_request()
#    else:
#        access_token = open(cookie('facebook')).read()
#
#    if not access_token:
#        raise GraphAPIError('Unable to login the user.')
#
#    return GraphAPI(access_token)


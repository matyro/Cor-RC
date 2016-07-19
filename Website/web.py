import tornado.ioloop
import tornado.web
import tornado.template

import tornado.httpserver

import os

##Websites import
from Website.site_index import IndexHandler

from Website.site_login import LoginHandler
from Website.site_logout import LogoutHandler
from Website.site_register import RegisterHandler

from Website.site_about import AboutHandler

from Website.site_main import MainHandler

from Website.site_steeringEdit import SteeringCardEditHandler
from Website.site_steeringShow import SteeringCardShowHandler

from Website.site_edit import EditHandler
from Website.site_rawPacket import RawPacketHandler


##loader = template.Loader('templates/')

settings = {
    'static_path': os.path.join(os.getcwd(), 'Website/static'),
    'template_path': os.path.join(os.getcwd(), 'Website/templates'),
    'cookie_secret': '__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__',
    'login_url': '/login',
    'xsrf_cookies': True,
    'debug':False
}

def make_web(sql_session): 
    
    return tornado.web.Application([
        (r'/', IndexHandler, dict(database=sql_session)),
        (r'/login', LoginHandler, dict(database=sql_session)),
        (r'/logout', LogoutHandler, dict(database=sql_session)),
        (r'/register', RegisterHandler, dict(database=sql_session)),
        (r'/about', AboutHandler, dict(database=sql_session)),
        (r'/main', MainHandler, dict(database=sql_session)),
        (r'/show_cards', SteeringCardShowHandler, dict(database=sql_session)),
        (r'/edit_card', SteeringCardEditHandler, dict(database=sql_session)),
		(r'/edit', EditHandler, dict(database=sql_session)),
        (r'/raw', RawPacketHandler, dict(database=sql_session))
    ], **settings)


def make_ssl(app):
    http_server = tornado.httpserver.HTTPServer(app, ssl_options={
        'certfile': 'keys/ca.csr',
        'keyfile': 'keys/ca.key',
    })
    http_server.listen(443)
    return http_server

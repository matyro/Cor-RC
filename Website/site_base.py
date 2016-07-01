import tornado.ioloop
import tornado.web
import tornado.template

import tornado.httpserver


import datetime
import pytz

from SQL.table_user import User


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self): # Sets current_user in every template       
        name = self.get_secure_cookie('user') 
        print('GetCurrentUser ' + str(name))
        if not name: 
            return None
        
        data =  tornado.escape.json_decode(name)
        usr = self.database.query(User).filter(User.username==str(data[0])).first()
        
        if usr is None:
            return None
        if usr.session_id is None:
            return None
        
        time = (datetime.datetime.now(pytz.utc).replace(tzinfo=None) - usr.session_date).total_seconds()
        if usr.session_id == data[1] and time < 3600:            
            return usr            
        
        return None

    def initialize(self, database):
        self.database = database

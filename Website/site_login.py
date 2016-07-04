from Website.site_base import BaseHandler

from SQL.table_user import User

import tornado.web
import random

class LoginHandler(BaseHandler):              
    @tornado.web.asynchronous
    def get(self):  
        if self.current_user is not None:
                self.redirect(self.get_argument('next','/'))
  
        error_msg = ''        
        for itr in self.get_arguments('error'):
            if itr == '1':
                error_msg = error_msg + 'Invalide password!\n'
            if itr == '2':
                 error_msg = error_msg + 'Username does not exist!\n'
        
        self.render('login.html', error=error_msg, next=self.get_argument('next','/'))
    
        
    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')             
        
        usr = self.database.query(User).filter(User.username==str(username)).first()
        if usr is None:
            error_msg = u'?error=' + tornado.escape.url_escape('2')
            self.redirect(u'/login' + error_msg + '&' + self.get_argument('next')) 
        elif usr.password == password: 
            print('Login ' + usr.username)
            cookie = usr.login( self.database, random.getrandbits(32) )
            self.set_secure_cookie('user', tornado.escape.json_encode(cookie))  
            print('uri: ' + str(self.request.uri))  
            print('path: ' + str(self.request.path))        
            self.redirect(self.get_argument('next', u'/main'))  
        else:
            error_msg = u'?error=' + tornado.escape.url_escape('1')
            self.redirect(u'/login' + error_msg + '&' + self.get_argument('next')) 

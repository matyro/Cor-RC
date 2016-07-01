from Website.site_base import BaseHandler

from SQL.table_user import User

import tornado.web
import random

class RegisterHandler(BaseHandler):
              
    @tornado.web.asynchronous
    @tornado.web.authenticated
    def get(self):  
        error_msg = ''        
        for itr in self.get_arguments('error'):
            if itr == '1':
                error_msg = error_msg + 'Invalide password!\n'
            if itr == '2':
                 error_msg = error_msg + 'Username does not exist!\n'  
               
        self.render('register.html',  error=error_msg)
    
        
    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')             
        
        usr = self.database.query(User).filter(User.username==str(username)).first()
        if usr is None: #user dont exists
            self.redirect('index.html') 
        else:   #user exists already     
            self.redirect('register.html')  
        

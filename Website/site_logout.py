from Website.site_base import BaseHandler

import tornado.web

class LogoutHandler(BaseHandler):
    @tornado.web.authenticated 
    def get(self):   
        if self.current_user is None:
            self.redirect(u'/')          
        else:
            self.current_user.logout(self.database)
            self.clear_cookie('user') 
            self.current_user = None
            self.redirect(u'/')

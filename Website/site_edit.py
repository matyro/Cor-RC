from Website.site_base import BaseHandler

import tornado.web

class EditHandler(BaseHandler):
    @tornado.web.authenticated 
    def get(self):   
        self.render('edit.html')

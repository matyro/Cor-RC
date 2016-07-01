from Website.site_base import BaseHandler

import tornado.web

class IndexHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):  
        if self.current_user is None:
            self.render('index.html')
        else:
            self.redirect(u'/main')

from Website.site_base import BaseHandler

import tornado.web

class AboutHandler(BaseHandler):
              
    @tornado.web.asynchronous    
    def get(self):        
        self.render('about.html')
    
        
  
        

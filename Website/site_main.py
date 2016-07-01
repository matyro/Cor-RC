from Website.site_base import BaseHandler

from SQL.table_simulation import Simulation

import tornado.web

class MainHandler(BaseHandler):           
    @tornado.web.authenticated  
    def get(self):            
        sim = self.database.query(Simulation).order_by(Simulation.startTime.desc()).all()
        self.render('main.html', simulation=sim)

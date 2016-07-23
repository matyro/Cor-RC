from Website.site_base import BaseHandler

from SQL.table_steeringcard import Steering_Card

import tornado.web

class SteeringCardEditHandler(BaseHandler):
    @tornado.web.authenticated  
    def get(self):  
        #if self.get_arguments('id'):
        #    tmp = self.database.query(Steering_Card).filter(Steering_Card.id==self.get_arguments('id')). \
        #                            filter( _or(Steering_Card.privat==False), _and(Steering_Card.privat==True, Steering_Card.user_id==self.current_user.id)).all()
        #    self.render('edit_steeringcard.html', steering=tmp)
            
        self.render('edit_steeringcard.html', steering=None)
        
    def post(self):
        return








































































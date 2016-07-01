from Website.site_base import BaseHandler

from SQL.table_steeringcard import Steering_Card

import tornado.web

class SteeringCardShowHandler(BaseHandler):
    @tornado.web.authenticated  
    def get(self):  
        card = []
        if self.get_arguments('id'):
            for itr in self.get_arguments('id'):
                card = card + self.database.query(Steering_Card).filter(Steering_Card.id==itr). \
                                                                      filter(Steering_Card.privat==False).all()
                card = card + self.database.query(Steering_Card).filter(Steering_Card.id==itr). \
                                                                      filter(Steering_Card.privat==True). \
                                                                      filter(Steering_Card.user_id==self.current_user.id).all()
        else:
            card = self.database.query(Steering_Card).filter(Steering_Card.user_id==self.current_user.id).order_by(Steering_Card.create_date.desc()).all()
       
    
        
            
        self.render('show_steeringcard.html', steering=card)

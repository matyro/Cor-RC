from Website.site_base import BaseHandler

import tornado.web
import tornado

import SQL.table_simulation as SQLsim



class RawPacketHandler(BaseHandler):
    @tornado.web.authenticated 
    def get(self):
        if self.current_user is None:
            self.redirect('login.html?next=edit')
            return			
        
        if self.current_user.permission < 9000:
            self.redirect('/')
            return                  
        
       
        sim = self.database.query(SQLsim.Simulation).filter( SQLsim.Simulation.status==1 ).all()        
                
        print('Sim: ' + str(sim))
        
        self.render('raw_packet.html', simulation=sim)
        
        self.database.commit()  #Important otherwise transactions are reused and cached data is used not (possible) new
         
        
    def post(self):               
        print(str(self.request))     
       
        print('Message: ' + str( self.get_argument('message', '')))
        print('Client: ' + str( self.get_argument('client', '')))
        print('header: ' + str( self.get_argument('header', '')))
        self.redirect('/raw')
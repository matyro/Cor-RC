from Website.site_base import BaseHandler

from SQL.table_steeringcard import Steering_Card

import tornado.web


class Setting(object):
    def __init__(self):
        self.name = 'empty name'
        self.content = '<a> content </a>'
        self.desc = 'Description_of this setting'


import xml.etree.ElementTree as etree 
def createSettings():
    tree = etree.parse('steering_75xx.xml')
    root = tree.getroot()
    for itr in root:
        #print(itr)
        #print(counter)
        counter += 1    
        
    print(counter)
    
    for el in root.getchildren():
        name = el.find('name').text
        for x in el.getchildren():
            print(x)

    


class SteeringCardEditHandler(BaseHandler):
    @tornado.web.authenticated  
    def get(self):  
        #if self.get_arguments('id'):
        #    tmp = self.database.query(Steering_Card).filter(Steering_Card.id==self.get_arguments('id')). \
        #                            filter( _or(Steering_Card.privat==False), _and(Steering_Card.privat==True, Steering_Card.user_id==self.current_user.id)).all()
        #    self.render('edit_steeringcard.html', steering=tmp)
            
        settings = []
        settings.append( Setting() )
        
        self.render('edit_steeringcard.html', steering=settings)
        
    def post(self):
        return








































































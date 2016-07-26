from Website.site_base import BaseHandler

from SQL.table_steeringcard import Steering_Card

import tornado.web


class Setting(object):
    def __init__(self, name, desc, content):
        self.name = name
        self.desc = desc
        self.content = str(content)


import xml.etree.ElementTree as etree 
def createSettings():
    tree = etree.parse('Corsika/steering/steering_75xx.xml')
    root = tree.getroot()
        
    list = []
    for el in root.getchildren():
        name = el.find('name').text
        desc = el.find('desc').text
        content = ''
        for x in el.find('parameter'):
           content = content + ', ' + str(x.find('name').text)

        list.append(Setting(name,desc,content))
    
    return list

class SteeringCardEditHandler(BaseHandler):
    @tornado.web.authenticated  
    def get(self):  
        #if self.get_arguments('id'):
        #    tmp = self.database.query(Steering_Card).filter(Steering_Card.id==self.get_arguments('id')). \
        #                            filter( _or(Steering_Card.privat==False), _and(Steering_Card.privat==True, Steering_Card.user_id==self.current_user.id)).all()
        #    self.render('edit_steeringcard.html', steering=tmp)
                   
       
        self.render('edit_steeringcard.html', steering=createSettings())
        
    def post(self):
        return








































































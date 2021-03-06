from Website.site_base import BaseHandler

from SQL.table_steeringcard import Steering_Card

import tornado.web


def xstr(s):
    if s is None:
        return ''
    return str(s)

class Setting(object):
    def __init__(self, name, desc, content):
        self.name = name
        self.desc = desc
        self.content = str(content)


import xml.etree.ElementTree as etree 
def createSettings():
    parameterCounter = 0
    tree = etree.parse('Corsika/steering/steering_75xx.xml')
    root = tree.getroot()
        
    list = []
    for el in root.getchildren():
        name = el.find('name').text
        desc = el.find('desc').text
        content = ''
        for x in el.find('parameter'):
            if x.find("format").text == 'I':
                content = content + '<div class=\"form-group\"><label id=\"tt\" title=\"' + xstr(x.find('desc').text)  + '\">'          
                content = content + xstr(x.find('name').text) + ':</label>'
                content = content + '<input type=\"number\" step=\"any\" class=\"inline input-sm \" name=\"' + xstr(x.find('name').text) + '\"'                
                content = content + '\" value=\"' + xstr(x.find('default').text) + '\"'
                content = content +  '/></div><!-- I -->'
                    
            elif x.find("format").text == 'F':
                content = content + '<div class=\"form-group\"><label id=\"tt\" title=\"' + xstr(x.find('desc').text)  + '\">'          
                content = content + xstr(x.find('name').text) + ':</label>'
                content = content + '<input type=\"number\" step=\"any\" class=\"inline input-sm \" name=\"' + xstr(x.find('name').text) + '\"'
                content = content + 'value=\"' + xstr(x.find('default').text) + '\"' 
                content = content + '/></div><!-- F -->'
                    
            elif x.find("format").text == 'L':
                content = content + '<div class=\"form-group\"><label id=\"tt\" title=\"' + xstr(x.find('desc').text)  + '\">'          
                content = content + xstr(x.find('name').text) + ':</label>'
                content = content + '<input type=\"checkbox\" class="inline" name=\"' + xstr(x.find('name').text) + '\"'
                content = content + 'value=\"' + xstr(x.find('default').text) + '\"' 
                content = content + '/></div><!-- L -->'                
                   
            else: 
                content = content + '<div class=\"form-group\"><label id=\"tt\" title=\"' + xstr(x.find('desc').text)  + '\">'          
                content = content + xstr(x.find('name').text) + ':</label>'
                content = content + '<input maxlength=\"256\" type=\"text\" class=\"inline input-sm \" name=\"' + xstr(x.find('name').text) + '\"'
                content = content + 'value=\"' + xstr(x.find('default').text) + '\"' 
                content = content + '/></div><!-- ELSE -->'
                
            parameterCounter = parameterCounter + 1
                
            content = content + '\n'           

        list.append(Setting(name,desc,content))
        
        
    print('Parameter Counter: ' + str(parameterCounter))
    return list

class SteeringCardEditHandler(BaseHandler):
    @tornado.web.authenticated  
    def get(self):  
        #if self.get_arguments('id'):
        #    tmp = self.database.query(Steering_Card).filter(Steering_Card.id==self.get_arguments('id')). \
        #                            filter( _or(Steering_Card.privat==False), _and(Steering_Card.privat==True, Steering_Card.user_id==self.current_user.id)).all()
        #    self.render('edit_steeringcard.html', steering=tmp)
                   
       
        self.render('edit_steeringcard.html', steering=createSettings(), steeringFiles=[])
        
    def post(self):
        print(self.request.arguments)
        return








































































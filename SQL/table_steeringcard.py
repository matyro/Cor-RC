from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, BigInteger, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import types
from sqlalchemy.sql import func
from sqlalchemy import update

from SQL.base import Base

import datetime
import pytz

print('Create SQL-SteeringCard')
class Steering_Card(Base):
        __tablename__ = 'Steering_Card'
        
        id = Column('id', Integer, primary_key=True)   
        
        local_id = Column('local_id', Integer)   
        inherit_id = Column('inherit_id', Integer, ForeignKey('Steering_Card.id', ondelete='SET NULL'), nullable=True)  
        
       
        name = Column('name', String(64)) 
        
        
        path = Column('path', String(512)) 
        
        
        create_date = Column('create_date', DateTime(), default=datetime.datetime.now(pytz.utc).replace(tzinfo=None))        
        
        user_id = Column('user_id', Integer, ForeignKey('User.id'), default=1) 
                
        ## CPU: /proc/cpuinfo
        ## MEM: /proc/meminfo
        
        #def __init__(self, data): 

        def __repr__(self):
                return "<Steering_Card(%s, %s, %s)>" % (self.id, self.name, self.user_id)

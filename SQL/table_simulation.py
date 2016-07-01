from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, BigInteger, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import types
from sqlalchemy.sql import func
from sqlalchemy import update

from SQL.base import Base

import datetime
import pytz

import enum


print('Create SQL-Simulation')

class SimulationStatus(enum.Enum):
    unknown = 0
    running = 1
    stopped = 2
    crashed = 3
   
            
class Simulation(Base):
        __tablename__ = 'Simulation'
        
        id = Column('id', Integer, primary_key=True)
        ip = Column('IP', String(39)) #IPv6 compatible
        
        startTime = Column('Start', DateTime(), default=datetime.datetime.now(pytz.utc).replace(tzinfo=None))
        
        endTime = Column('End', DateTime())
        status = Column('Status', Integer, default=SimulationStatus.unknown.value)
        
        profile = Column ('profile', String(32), default='')     
        
        steering_card_id = Column('steering_card_id', Integer, default=1)        
        
        hostname = Column('hostname', String(32), default='')
        
        user_id = Column('user_id', Integer, ForeignKey('User.id'), default=1)       
        
        events = Column('events', Integer, default=0)
        
        ## CPU: /proc/cpuinfo
        ## MEM: /proc/meminfo
        
        #def __init__(self): 
           

        def __repr__(self):
                return "<Simulation(%s, %s, %s)>" % (self.id, self.ip, self.profile)     

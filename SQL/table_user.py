from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, BigInteger, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import types
from sqlalchemy.sql import func
from sqlalchemy import update

from SQL.base import Base


print('Create SQL-User')

class User(Base):
    __tablename__ = 'User'
        
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(32), nullable=False, unique=True)
    fullname = Column('fullname', String(64), default='')
        
    password = Column('password',  String(32), nullable=False)
    salt = Column('salt',  String(32))
        
    email = Column('email', String(128), default='')
    permission = Column('permission', Integer(), default=1)
        
    session_id = Column('session_id', BigInteger())
    session_date = Column('lastLogin', DateTime())
                    
    steering_cards = relationship('Steering_Card', backref='user')    
    simulations = relationship('Simulation', backref='user') 

    def __repr__(self):
        return '<Username(%s, %s, %s, %s)>' % (self.id, self.username, self.fullname, self.email)
             
    def login(self, session, sessionID):
        self.session_id = sessionID
        self.session_date = func.utc_timestamp()
        session.commit()        
        return (self.username, sessionID)
    
    def logout(self, session):
        self.session_id = 0
        session.commit()  

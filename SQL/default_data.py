import random
import string

import SQL.base

from SQL.table_user import User
from SQL.table_steeringcard import Steering_Card

def default_user(session):
    dummy = User(username='', password=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(32)))
    admin = User(username='dbaack', fullname='Dominik Baack', password='abcd', email='dominik.baack@udo.edu', permission='9999')       
    try:
        session.add(dummy)
        session.add(admin)    
        session.commit()
    except:
        session.rollback()
        pass


def default_steeringcard(session):
    try:
        testCard1 = Steering_Card(card='', name='dummy', user=dummy)        
        session.add(testCard1)        
        session.commit()
    except:
        session.rollback()
        pass




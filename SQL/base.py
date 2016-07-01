from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()




from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#engine://user:password@host:port/database
def createSession(url):
    engine = create_engine(url, pool_recycle=3600) 
    engine.echo = False  #Output

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    return {'session':session, 'engine':engine}




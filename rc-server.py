
import Website.web as web

import Corsika.CorsikaManager as cor

import SQL.base as sql
import SQL.default_data as sql_default


import tornado  #PeriodicCallback
from sqlalchemy import exc

import time

def start_web(sql_session):
    print('Create webservice')
    app = web.make_web(sql_session)
    web_server = tornado.httpserver.HTTPServer(app)    
    web_server.bind(10003)    
    web_server.start(1)
    return web_server


def start_corsika(sql_session):
    print('Create corsika connection')
    corsika_server = cor.CorsikaManager()
    corsika_server.bind(10004)
    corsika_server.start(1)  # Forks multiple sub-processes
    return corsika_server


def stop(sql_session):
    print('Close tornado')
    tornado.ioloop.IOLoop.current().stop()
    print('Close SQL')
    sql_session.close()


t0 = time.time()
periodic_counter = 0
def periodic_callback1(sql_session, sql_engine):
    global periodic_counter

    if(periodic_counter == 30):
        print('Uptime: ' + str(round(time.time() - t0)) + ' seconds')
        periodic_counter = 0
    periodic_counter += 1

    try:
        sql_engine.execute("SELECT 1")  # could also be .ping(),
                                    # not sure what is better
    except (exc.OperationalError, ex):
        if ex.args[0] in (2006,   # MySQL server has gone away
                          2013,   # Lost connection to MySQL server during query
                          2055):  # Lost connection to MySQL server at '%s', system error: %d
            # caught by pool, which will retry with a new connection
            print('Disconnected')
            raise exc.DisconnectionError()
        else:
            raise


    return



if __name__ == '__main__':

    print('Connect to SQL Database')
    session = sql.createSession('mysql+pymysql://dbaack:1245@vollmond.app.tu-dortmund.de:10000/Corsika')
    
    print('Create default entrys')
    sql_default.default_user(session['session'])
    sql_default.default_steeringcard(session['session'])


    start_web(session['session'])
    
    start_corsika(session['session'])    


    periodic1 = tornado.ioloop.PeriodicCallback(lambda: periodic_callback1(session['session'], session['engine']), 2000)
    periodic1.start()

    try:
        print('Start tornado')
        tornado.ioloop.IOLoop.current().start()
       

    except (KeyboardInterrupt, SystemExit):
        print('Exception INT or EXIT')
        
    periodic1.stop()
    stop(session['session'])        

else:
    print('Start this program as main application')


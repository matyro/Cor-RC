
import Website.web as web

import Corsika.CorsikaManager as cor

import SQL.base as sql
import SQL.default_data as sql_default


import tornado  #PeriodicCallback

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

if __name__ == '__main__':

    print('Connect to SQL Database')
    session = sql.createSession('mysql+pymysql://dbaack:1245@vollmond.app.tu-dortmund.de:10000/Corsika')
    
    print('Create default entrys')
    sql_default.default_user(session['session'])
    sql_default.default_steeringcard(session['session'])


    start_web(session['session'])
    
    start_corsika(session['session'])    

    try:
        print('Start tornado')
        tornado.ioloop.IOLoop.current().start()
       

    except (KeyboardInterrupt, SystemExit):
        print('Exception INT or EXIT')
        
        
    stop(session['session'])        

else:
    print('Start this program as main application')


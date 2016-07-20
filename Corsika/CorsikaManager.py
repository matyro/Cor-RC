
import tornado
from tornado.tcpserver import TCPServer

import threading


import Corsika.CorsikaClient as CC

class CorsikaManager(TCPServer):
    
    con_list = dict()
    lock = threading.Lock()
    
    @tornado.gen.coroutine
    def handle_stream(self, stream, address):
        
        connection = CC.CorsikaClient(stream, self)
        CorsikaManager.lock.acquire()
        try:
            CorsikaManager.con_list[connection.id] = connection
            print("New connection: %s"%connection.id)
        finally:
            CorsikaManager.lock.release()
        
        yield connection.on_connect()
        
        #print('TCP: ' + str(stream) + ' | ' + str(address))
        #print('Message: ' + str(stream.read_bytes(5).result()) )
        

    def remove_con(self, id):
        CorsikaManager.lock.acquire()
        try:
              CorsikaManager.con_list.pop(id)
        except KeyError:
            print('KeyError for remove_con CorsikaManager: This should never happen!')
            pass
        finally:
            CorsikaManager.lock.release()
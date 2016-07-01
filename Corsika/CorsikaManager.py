
import tornado
from tornado.tcpserver import TCPServer



import Corsika.CorsikaClient as CC

class CorsikaManager(TCPServer):
    
    @tornado.gen.coroutine
    def handle_stream(self, stream, address):
        
        connection = CC.CorsikaClient(stream)
        yield connection.on_connect()
        
        #print('TCP: ' + str(stream) + ' | ' + str(address))
        #print('Message: ' + str(stream.read_bytes(5).result()) )
        

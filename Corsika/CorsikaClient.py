import tornado
from tornado.tcpserver import TCPServer
 

import datetime
import pytz

import struct
   

class CorsikaClient(object):
    client_id = 0

    def __init__(self, stream, manager):
        super().__init__()
        CorsikaClient.client_id += 1
        
        self.id = CorsikaClient.client_id
        self.stream = stream
        self.manager = manager

        #self.stream.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # Deactivates packet collection to bigger ones
        #self.stream.socket.setsockopt(socket.IPPROTO_TCP, socket.SO_KEEPALIVE, 1) # activates keep_alive message
        self.stream.set_close_callback(self.on_disconnect)


    @tornado.gen.coroutine
    def on_disconnect(self):
        self.manager.remove_con(self.id)
        self.log("disconnected")
        yield []

    @tornado.gen.coroutine
    def dispatch_client(self):
        try:
            while True:               
                header_raw = yield self.stream.read_bytes(8)
                header = struct.unpack("<I I", header_raw)                

                self.log('Length: |%s Byte|' % header[0])
                self.log('Header: |%s|' % header[1])
                if header[0] > 8:
                    data = yield self.stream.read_bytes(header[0] - 8) #returnes bytes
                    try:
                         self.log('Pass : |%s| to callback' % header[1])
                        #callback[header](data)   
                    except KeyError:
                        continue
                    
                else:    
                    try:
                        self.log('Pass : |%s| to callback without data' % header[1])
                        #callback[header](b'')     
                    except KeyError:
                        continue
                                
                                
                #yield self.stream.write(line)
        except tornado.iostream.StreamClosedError:
            pass

    @tornado.gen.coroutine
    def on_connect(self):
        raddr = 'closed'
        try:
            raddr = '%s:%d' % self.stream.socket.getpeername()
        except Exception:
            pass
        self.log('new, %s' % raddr)
        yield self.dispatch_client()

    def log(self, msg, *args, **kwargs):
        print('[connection %d] %s' % (self.id, msg.format(*args, **kwargs)))

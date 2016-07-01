import tornado
from tornado.tcpserver import TCPServer
 

import datetime
import pytz

import struct
   

class CorsikaClient(object):
    client_id = 0

    def __init__(self, stream):
        super().__init__()
        CorsikaClient.client_id += 1
        self.id = CorsikaClient.client_id
        self.stream = stream

        #self.stream.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # Deactivates packet collection to bigger ones
        #self.stream.socket.setsockopt(socket.IPPROTO_TCP, socket.SO_KEEPALIVE, 1) # activates keep_alive message
        self.stream.set_close_callback(self.on_disconnect)


    @tornado.gen.coroutine
    def on_disconnect(self):
        self.log("disconnected")
        yield []

    @tornado.gen.coroutine
    def dispatch_client(self):
        try:
            while True:               
                length_byte = yield self.stream.read_bytes(8)
                header = struct.unpack("<I I", length_byte)                

                self.log('Length: |%s Byte|' % header[0])
                self.log('Header: |%s|' % header[1])
                data = yield self.stream.read_bytes(header[0])
                self.log('got |%s|' % data.decode('utf-8').strip())
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

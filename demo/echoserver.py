# -*- coding: utf-8 -*-
"""
Created on 2014/12/25
@author: LEO
"""


import asyncore
import socket

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.send(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = EchoHandler(sock)

    # def handle_read(self):
    #     data = self.recv(1028)
    #     print 'recieve data from client '
    #     print data
    #     pass







if __name__ == '__main__':
    server = EchoServer('192.168.117.117', 8080)
    asyncore.loop()
    pass

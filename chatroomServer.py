# -*- coding: utf-8 -*-

import socket
import threading
import select
import sys

#multi-version support
version = sys.version[0]
if version == '2':
    import Queue as Queue
elif version == '3':
    import queue as Queue

port = 10001
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(False)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR  , 1)
server_address = ('0.0.0.0',port)
server.bind(server_address)
server.listen(5)

#sockets from which we except to read
inputs = [server]
 
#sockets from which we expect to write
outputs = []
 
#Outgoing message queues (socket:Queue)
message_queues = {}
 
#A optional parameter for select is TIMEOUT
timeout = 20000

def func():
    while True:
        print('System: server now is listening on port ' + str([port]))
        readable , writable , exceptional = select.select(inputs, outputs, inputs, timeout)
        if not (readable or writable or exceptional) :
                print ("Time out ! ")
                break
        for s in readable :
            if s is server:
                # A "readable" socket is ready to accept a connection
                connection, client_address = s.accept()
                print ("    connection from ", client_address)
                connection.setblocking(0)
                inputs.append(connection)
                message_queues[connection] = Queue.Queue()
            else:
                data = s.recv(1024).decode()
                if data :
                    print (" received " , [data] , "from ",s.getpeername())
                else:
                    #Interpret empty result as closed connection
                    print ("  closing", client_address)
                    inputs.remove(s)
                    s.close()
                    #remove message queue 
                    del message_queues[s]

if __name__ == '__main__':
    func()
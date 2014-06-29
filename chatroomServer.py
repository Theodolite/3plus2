# -*- coding: utf-8 -*-

import socket

port = 10001
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('0.0.0.0',port)
server.bind(server_address)
server.listen(5)

while True:
    print 'System: server now is listening on port ' + str([port])
    connection, client_address = server.accept()
    print 'System: ' + str(client_address) + ' is connected'

    while True:
        try:
            data = connection.recv(1024)
            print('From client: ' + data)
            connection.send(data)
        except:
            print("System: client has quitted\n")
            break

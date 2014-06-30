# -*- coding: utf-8 -*-

import socket
import threading

def server1():
    port = 10001
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = ('0.0.0.0',port)
    server.bind(server_address)
    server.listen(1)

    while True:
        print('System: server now is listening on port ' + str([port]))
        connection, client_address = server.accept()
        print('System: ' + str(client_address) + ' is connected')

        while True:
            try:
                data = connection.recv(1024).decode()
                print('From client: ' + data)
                connection.send(data.encode())
            except:
                print("System: client has quitted\n")
                break
def server2():
    port = 10002
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = ('0.0.0.0',port)
    server.bind(server_address)
    server.listen(0)

    while True:
        print('System: server now is listening on port ' + str([port]))
        connection, client_address = server.accept()
        print('System: ' + str(client_address) + ' is connected')

        while True:
            try:
                data = connection.recv(1024).decode()
                print('From client: ' + data)
                connection.send(data.encode())
            except:
                print("System: client has quitted\n")
                break

if __name__ == '__main__':
    t1 = threading.Thread(target = server1)
    t1.start()

    t2 = threading.Thread(target = server2)
    t2.start()
    server2()
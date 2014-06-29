# -*- coding: utf-8 -*-

import socket

server_address = ("127.0.0.1",10001)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.connect(server_address)

while True:
    data = raw_input("To server: ")
    server.send(data)
    msg = server.recv(1024)
    print("from server: " + str(msg))
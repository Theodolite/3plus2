# -*- coding: utf-8 -*-

import socket
import sys

version = sys.version[0]
if version == '2':
    input = raw_input
elif version == '3':
    input = input

server_address = ("127.0.0.1",10001)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.connect(server_address)

while True:
    data = input("To server: ")
    if data:
        server.send(data.encode())
        msg = server.recv(1024).decode()
        print("from server: " + str(msg))
    else:
        print("Null message is not allowed!")

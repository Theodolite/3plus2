# -*- coding: utf-8 -*-

import socket
import sys
import threading

version = sys.version[0]
if version == '2':
    input = raw_input
elif version == '3':
    input = input

server_address = ("127.0.0.1",10001)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    server.connect(server_address)
except:
    print("error")
    input()

def func_send():
    while True:
        data = input("To server: ")
        if data:
            server.send(data.encode())
            #msg = server.recv(1024).decode()
            #print("from server: " + str(msg))
        else:
            print("Null message is not allowed!")

def func_recv():
    while True:
        data = server.recv(1024).decode()
        print("From server " + data)

if __name__ == '__main__':
    thread_send = threading.Thread(target = func_send)
    thread_recv = threading.Thread(target = func_recv)

    thread_send.start()
    thread_recv.start()

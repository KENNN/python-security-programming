#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

if __name__ == "__main__" :
    ip = '127.0.0.1'
    port = 50000
    server = (ip, port)
    msg = ''

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server)

        while msg != 'exit' :
            msg = input('> ')
            s.send(msg.encode())
            data = s.recv(1024)
            print('Received from server: {}'.format(data.decode()))
#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 50000
    server = (ip, port)
    data = ''

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(server)
        s.listen(1)
        print('Waiting connection ...')


        connection, address = s.accept()
        with connection:
            print('Connection from {}'.format(str(address)))

            while True :
                data = connection.recv(1024)
                print('Received a message: {}'.format(data.decode()))

                if data == b'exit':
                    term = 'OK, Good Bye'
                    connection.send(term.encode())
                    print('Sent a message: {}'.format(term))
                    break
                else:
                    connection.send(data)
                    print('Sent a message: {}'.format(data.decode()))


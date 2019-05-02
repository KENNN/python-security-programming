#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys
import click


@click.command()
@click.argument('ip')
def scan(ip):
    ports = range(1, 10000)

    for port in ports:
        sock = socket.socket()
        ret = sock.connect_ex((ip, port))

        if ret == 0:
            print('{} open'.format(port))


def main():
    scan()


if __name__ == "__main__":
    main()

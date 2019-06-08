#!/usr/bin/python
# -*- coding: utf-8 -*-

from scapy.ansmachine import AnsweringMachine
from scapy.all import conf
import socket
import click


class WlanSniffer(AnsweringMachine):
    function_name = 'WLAN Sniffer2'
    filter = "tcp dst port 443"

    def is_request(self, req):
        domain = ''
        try:
            domain = socket.gethostbyaddr(req['IP'].dst)[0]
        except socket.herror:
            domain = 'Unknown Host'

        summary = domain + ': ' + req.summary()
        print(summary)

        return False

    def make_request(self, req):
        return req


@click.command()
@click.argument('iface')
def run(iface):
    conf.iface = iface
    WlanSniffer()()


if __name__ == '__main__':
    run()

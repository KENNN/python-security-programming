#!/usr/bin/python
# -*- coding: utf-8 -*-

from scapy.ansmachine import AnsweringMachine
from scapy.all import conf
import click


class WlanSniffer(AnsweringMachine):
    function_name = 'WLAN Sniffer'
    filter = ""

    def is_request(self, req):
        print(req.summary())
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

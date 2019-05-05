#!/usr/bin/python
# -*- coding: utf-8 -*-

from scapy.all import Ether
from scapy.all import ARP
from scapy.all import srp
import ipaddress
import click


def gen_cidr(ip, netmask):
    ipv4 = ipaddress.ip_address(ip)
    netmask = ipaddress.ip_address(netmask)
    netaddr = ipaddress.ip_address(int(ipv4) & int(netmask))
    netaddr = str(netaddr).split('/')[0]
    cidr = bin(int(netmask)).count('1')
    return '{}/{}'.format(netaddr, cidr)


@click.command()
@click.argument('myip')
@click.argument('netmask')
def scan(myip, netmask):
    hwaddr = 'ff:ff:ff:ff:ff:ff'
    cidr = gen_cidr(myip, netmask)
    print('Scanning on: {}'.format(cidr))

    pkt = Ether(dst=hwaddr)/ARP(op=1, pdst=cidr)
    ans, uans = srp(pkt, timeout=2)

    for send, recv in ans:
        print(recv.sprintf('%ARP.psrc% is up'))


def main():
    scan()


if __name__ == "__main__":
    main()
#!/usr/bin/python
# -*- coding: utf-8 -*-

from scapy.all import IP
from scapy.all import ICMP
from scapy.all import sr1
import ipaddress
import click


def gen_iplist(ip, netmask):
    ipv4 = ipaddress.ip_address(ip)
    netmask = ipaddress.ip_address(netmask)
    netaddr = ipaddress.ip_address(int(ipv4) & int(netmask))
    netaddr = str(netaddr).split('/')[0]

    cidr = bin(int(netmask)).count('1')
    network_str = '{}/{}'.format(netaddr, cidr)
    print(network_str)
    ip_network = ipaddress.ip_network(network_str)

    return ip_network.hosts()


@click.command()
@click.argument('myip')
@click.argument('netmask')
def scan(myip, netmask):
    ip_list = gen_iplist(myip, netmask)

    for ip in ip_list:
        pkt = IP(dst=str(ip), ttl=64)/ICMP()
        reply = sr1(pkt, timeout=3)

        if reply is not None:
            print('{} is up.'.format(str(ip)))


def main():
    scan()


if __name__ == "__main__":
    main()

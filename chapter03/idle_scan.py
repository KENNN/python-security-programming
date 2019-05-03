#!/usr/bin/python
# -*- coding: utf-8 -*-

from scapy.all import IP
from scapy.all import TCP
from scapy.all import send
import click


def send_tcp(src_ip, dst_ip, port, flags):
    ip = IP(src=src_ip, dst=dst_ip)
    tcp = TCP(dport=(port), flags=flags)
    pkt = IP/TCP
    send(pkt)


def sr_tcp(src_ip, dst_ipm, port, flags):
    ip = IP(src=src_ip, dst=dst_ip)
    tcp = TCP(dport=(port), flags=flags)
    pkt = IP/TCP
    return sr1(pkt)


@click.command()
@click.argument('target_host')
@click.argument('idle_host')
@click.argument('idle_port')
def scan():
    ports = range(1, 1024)

    for target_port in ports:
        pkt1 = sr_tcp('127.0.0.1', target_host, idle_port, "SA")
        send_tcp(idle_host, target_host, target_port, "SA")
        pkt2 = sr_tcp('127.0.0.1', idle_host, idle_port, "SA")

        if pkt2.id - pkt1 >= 2:
            print('{} open'.format(target_port))
        else:
            pass


def main():
    scan()


if __name__ == "__main__":
    scan()

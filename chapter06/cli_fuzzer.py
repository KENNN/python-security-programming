#!/usr/bin/python
# -*- coding: utf-8 -*-

import click


class Fuzzer(object):
    def __init__(self):
        pass

    def gen_fuzz(self):
        pass

    def do_fuzz(self):
        pass

    def dump(self):
        pass


@click.command()
@click.argument('target_ip')
def run(target_ip):
    fuzzer = Fuzzer()
    while 1:
        fuzzer.gen_fuzz()
        ret_code = fuzzer.do_fuzz()
        if ret_code > 0:
            fuzzer.dump()


def main():
    run()


if __name__ == '__main__':
    main()

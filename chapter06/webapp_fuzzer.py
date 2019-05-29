#!/usr/bin/python
# -*- coding:utf: 8 -*-

import click


class WebAppFuzzer(object):
    def __init__(self, host, port):
        pass

    def gen_fuzz(self):
        pass

    def gen_fuzz(self):
        pass

    def do_fuzz(self):
        pass

    def is_vulnerable(self):
        pass

    def dump(self):
        pass


@click.command()
@click.argument('host')
@click.argument('port')
def run(host, port):
    fuzzer = WebAppFuzzer(host, port)

    while 1:
        fuzz = fuzzer.gen_fuzz()
        response = fuzzer.do_fuzz(fuzz)
        if fuzzer.is_vulnerable():
            fuzzer.dump()


def main():
    run()


if __name__ == '__main__':
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-

import click
import string
import random


class Fuzzer(object):
    def __init__(self, target):
        self.target = target
        self.alnum = string.digits + string.ascii_letters
        self.rand = random.SystemRandom()

    def gen_fuzz(self):
        rand_int = self.rand.randint(1, 64)
        fuzz = random.choices(self.alnum, k=rand_int)
        fuzz = ''.join(fuzz)
        return fuzz

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

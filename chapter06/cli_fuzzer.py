#!/usr/bin/python
# -*- coding: utf-8 -*-

import click
import string
import random
import subprocess


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

    def do_fuzz(self, fuzz):
        cmd = ' '.join([self.target, fuzz])
        ret = subprocess.run(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        ret_code = ret.returncode
        return ret_code

    def dump(self):
        pass


@click.command()
@click.argument('target')
def run(target):
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

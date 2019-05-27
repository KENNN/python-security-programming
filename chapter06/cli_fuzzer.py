#!/usr/bin/python
# -*- coding: utf-8 -*-

import click
import string
import random
import sys
import subprocess
from subprocess import PIPE


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

    def dump(self, fuzz, ret_code):
        data = '{},{}\n'.format(ret_code, fuzz)
        with open('dump.csv', 'a') as f:
            f.write(data)


@click.command()
@click.argument('target')
def run(target):
    fuzzer = Fuzzer(target)
    fuzz_cnt = 0
    crash = 0

    while 1:
        fuzz = fuzzer.gen_fuzz()
        fuzz_cnt += 1
        ret_code = fuzzer.do_fuzz(fuzz)
        if ret_code > 0:
            crash += 1
            fuzzer.dump(fuzz, ret_code)

        sys.stdout.write(
            '\rfuzz: {}, crashes: {}'.format(fuzz_cnt, crash))
        sys.stdout.flush()


def main():
    run()


if __name__ == '__main__':
    main()

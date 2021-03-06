#!/usr/bin/python
# -*- coding:utf: 8 -*-

import click
import glob
import string
import socket
import urllib.parse
import time
import sys
import re


class WebAppFuzzer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)

        files = glob.glob('./fuzzdb/attack/xss/**/*.txt', recursive=True)
        self.fuzzdb = []

        for fname in files:
            with open(fname, 'rb') as f:
                data = f.read().decode('utf-8').splitlines()
                self.fuzzdb += data

        with open('./http_template.txt', 'rb') as f:
            data = f.read().decode('utf-8').replace('\n', '\r\n')
            self.http_template = string.Template(data)

        self.status_code = 0

    def gen_fuzz(self, index):
        return self.fuzzdb[index]

    def do_fuzz(self, fuzz):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            fuzz = urllib.parse.quote(fuzz)
            request = self.http_template.substitute(param=fuzz)
            s.send(request.encode('utf-8'))

            time.sleep(0.05)
            response = ''
            while 1:
                buf = s.recv(1024).decode('utf-8')
                response += buf
                if len(buf) < 1024:
                    break

        return response

    def is_vulnerable(self, fuzz, response):
        ptn = '[1-5][0-5][0-9]'
        match = re.search(ptn, response)
        self.status_code = int(match.group(0))

        if self.status_code >= 500:
            return True

        if fuzz in response:
            return True

        return False

    def dump(self, fuzz):
        data = str(self.status_code) + ',' + fuzz + '\n'
        with open('dump.txt', 'a') as f:
            f.write(data)


@click.command()
@click.argument('host')
@click.argument('port')
def run(host, port):
    fuzzer = WebAppFuzzer(host, port)

    dump_cnt = 0
    len_fuzzdb = len(fuzzer.fuzzdb)
    print('{} fuzz'.format(len_fuzzdb))
    for i in range(len_fuzzdb):
        fuzz = fuzzer.gen_fuzz(i)
        print('{}: {}'.format(i, fuzz))
        response = fuzzer.do_fuzz(fuzz)
        if fuzzer.is_vulnerable(fuzz, response):
            dump_cnt += 1
            fuzzer.dump(fuzz)

        sys.stdout.write('\rfuzz: {}, dumped: {}'.format(i + 1, dump_cnt))
        sys.stdout.flush()
        print('')


def main():
    run()


if __name__ == '__main__':
    main()

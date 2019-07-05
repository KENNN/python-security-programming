#!/usr/bin/python
# -*- coding:utf-8 -*-


import click


def solve(cipher, e):
    plaintext = []

    for c in cipher:
        m = int(round(c ** (1. / e)))
        plaintext.append(chr(m))

    return ''.join(plaintext)


def run():
    pass


def main():
    run()


if __name__ == "__main__":
    main()

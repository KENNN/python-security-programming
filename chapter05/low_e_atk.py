#!/usr/bin/python
# -*- coding:utf-8 -*-


import click


def solve(cipher, e):
    plaintext = []

    for c in cipher:
        m = int(round(c ** (1. / e)))
        plaintext.append(chr(m))

    return ''.join(plaintext)


@click.command()
@click.argument('e', type=int)
def run(e):
    cipher = [
        373248, 1157625, 85184, 32768,
        357911, 1030301, 1367631, 1481544,
        1092727, 1030301, 35937
    ]
    result = solve(cipher, e)

    print('plaintext:\n{}'.format(result))


def main():
    run()


if __name__ == "__main__":
    main()

#!/usr/bin/python
# -*- coding:utf-8 -*-


def ex_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = ex_gcd(b % a, a)
        return (gcd, y - int(b / a) * a, x)


def gen_private_key(e, phi_n):
    gcd, d, y = ex_gcd(e, phi_n)
    if d < 0:
        d += phi_n
    return d


def decrypt(cipher):
    pass


def run():
    pass


def main():
    run()


if __name__ == '__main__':
    main()

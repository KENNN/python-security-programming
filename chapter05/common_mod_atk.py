#!/usr/bin/python
# -*- coding:utf-8 -*-


import click


def ex_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = ex_gcd(b % a, a)
        return (gcd, y - int(b / a) * x, x)


def decrypt(c1, c2, e1, e2, N):
    _, s1, s2, = ex_gcd(e1, e2)

    if s1 < 0:
        _, c1, _ = ex_gcd(c1, N)
    elif s2 < 0:
        _, c2, _ = ex_gcd(c2, N)

    m1 = pow(c1, abs(s1), N)
    m2 = pow(c2, abs(s2), N)
    m = (m1 * m2) % N
    return chr(m)


def run():
    pass


def main():
    run()


if __name__ == "__main__":
    main()

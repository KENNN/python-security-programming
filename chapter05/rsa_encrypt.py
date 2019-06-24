#!/usr/bin/python
# -*- coding: utf-8 -*-


def gen_public_key(p, q):
    e = 65537
    n = p * q
    return e, n


def encrypt(plaintext):
    p, q = 513131, 248021
    e, n = gen_public_key(p, q)
    plaintext = list(plaintext)
    cipher = []

    for t in plaintext:
        c = pow(t, e, n)
        cipher.append(c)

    return cipher


def run():
    pass


def main():
    run()


if __name__ == '__main__':
    main()

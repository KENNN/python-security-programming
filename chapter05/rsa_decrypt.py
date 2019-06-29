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
    e = 65537
    p, q = 513131, 248021
    n = p * q
    phi_n = (p - 1) * (q - 1)
    plaintext = []

    d = gen_private_key(e, phi_n)

    for c in cipher:
        m = pow(c, d, n)
        plaintext.append(chr(m))
    return ''.join(plaintext)


def run():
    cipher = [
        86236114022, 40684851533, 4769316302, 30262751191,
        58094127192, 118116081811, 48679148382, 1197296142,
        77325435548, 118116081811, 39317881150
    ]
    plaintext = decrypt(cipher)
    print('plaintext:\n{}'.format(plaintext))


def main():
    run()


if __name__ == '__main__':
    main()

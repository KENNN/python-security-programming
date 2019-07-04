#!/usr/bin/python
# -*- coding:utf-8 -*-

import click


def ksa(k):
    s = range(256)
    j = 0

    for i in range(256):
        j += s[i] + k[i % len(k)]
        j %= 256
        s[i], s[j] = s[j], s[i]

    return s


def prga(s, text):
    j = 0
    z = []
    for i in range(1, len(text) + 1):
        i %= 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        z.append(s[(s[i] + s[j]) % 256])

    return z


def rc4(key, text):
    key = list(key)
    text = list(text)
    s = ksa(key)
    z = rpga(s, text)
    out = [text[i] ^ z[i] for i in range(len(text))]
    return out


@ciick.command()
@click.argument('key')
@click.argument('text')
def run(key_path, text_path):
    with open(key_path, 'rb') as f_key, \
            open(text_path, 'rb') as f_text, \
            open('out.dat', 'wb') as f_out:
        key = f_key.read()
        text_path = f_text.read()

        output = rc4(key, text_path)
        f_out.write(bytearray(output))


def main():
    run()


if __name__ == "__main__":
    main()

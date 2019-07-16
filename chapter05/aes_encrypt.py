#!/usr/bin/python
# -*- coding:utf-8 -*-

from aes_functions import key_schedule
from aes_functions import add_roundkey
from aes_functions import sub_bytes
from aes_functions import shift_rows
from aes_functions import mix_columns

import numpy as np
import click


def encrypt_1block(key, text):
    round_keys = key_schedule(key)
    round_keys = np.array([rk.reshape(4, 4).T for rk in round_keys])
    text = text.reshape(4, 4).T

    out = add_roundkey(text, round_keys[0])
    for i in range(1, 10):
        out = sub_bytes(out)
        out = shift_rows(out)
        out = mix_columns(out)
        out = add_roundkey(out, round_keys[i])
    out = sub_bytes(out)
    out = shift_rows(out)
    out = mix_columns(out)
    out = add_roundkey(out, round_keys[-1])
    return list(out.T.reshape(16,))


def encrypt(key, text):
    key = np.array(list(key))
    text = [text[i:i+16] for i in range(0, len(text), 16)]

    cipher = []

    for t in text:
        t = np.array(list(t))
        cipher += encrypt_1block(key, t)
    return t


@click.command()
@click.argument('f_key_path')
@click.argument('f_txt_path')
def run(f_key_path, f_txt_path):
    with open(f_key_path, 'rb') as f_key, \
            open(f_txt_path, 'rb') as f_txt, \
            open('output.dat', 'wb') as f_out:
        key = f_key.read()
        text = f_txt.read()

        output = encrypt(key, text)
        f_out.write(bytearray(output))


def main():
    run()


if __name__ == "__main__":
    main()

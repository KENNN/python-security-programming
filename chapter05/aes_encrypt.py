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


def run():
    pass


def main():
    pass


if __name__ == "__main__":
    main()

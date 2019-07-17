#!/usr/bin/python
# -*- coding: utf-8 -*-

from aes_functions import key_schedule
from aes_functions import add_roundkey
from aes_functions import inv_sub_bytes
from aes_functions import inv_shift_rows
from aes_functions import inv_mix_columns
import numpy as np
import sys


def decrypt_1block(key, enc):
    roundkeys = key_schedule(key)
    roundkeys = np.array([rk.reshape(4, 4).T for rk in roundkeys])
    enc = enc.reshape(4, 4).T

    out = add_roundkey(enc, roundkeys[-1])
    out = inv_shift_rows(out)
    out = inv_sub_bytes(out)
    for i in range(1, 10)[::-1]:
        out = add_roundkey(out, roundkeys[i])
        out = inv_mix_columns(out)
        out = inv_shift_rows(out)
        out = inv_sub_bytes(out)
    out = add_roundkey(out, roundkeys[0])
    return list(out.T.reshape(16,))


def decrypt(key, data):
    key = np.array(list(key))
    data = [data[i:i+16] for i in range(0, len(data), 16)]  # split per 16 byte
    plain = []

    for d in data:
        d = np.array(list(d))
        plain += decrypt_1block(key, d)
    return plain


if __name__ == '__main__':
    f_key = open(sys.argv[1], 'rb')
    f_enc = open(sys.argv[2], 'rb')
    key = f_key.read()
    enc = f_enc.read()

    output = decrypt(key, enc)
    f_out = open('output.dat', 'wb')
    f_out.write(bytearray(output))

    f_key.close()
    f_enc.close()
    f_out.close()

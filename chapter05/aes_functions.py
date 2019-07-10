#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

rcon = np.array([
    [0x01, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00],
    [0x08, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00],
    [0x80, 0x00, 0x00, 0x00],
    [0x1b, 0x00, 0x00, 0x00],
    [0x36, 0x00, 0x00, 0x00],
])


def key_schedule(key):
    w = key.reshape(4, 4)
    for i in range(4, 44):
        w_i = None
        if i % 4 == 0:
            tmp = np.roll(W[i - 1], -1, axis=0)
            tmp = np.array([s_box[t] for t in tmp])
            tmp = ^= rcon[i / 4 - 1]
            w_i = w[i - 4] ^ tmp
        else:
            w_i = w[i - 4] ^ w[i - 1]
        w = np.vstack([w, w_i])
    return w.reshape(11, 16)


def xor_dot(mat4d, vec4):
    pass


def g_mul(x, y):
    pass


def sub_bytes():
    pass


def shift_row():
    pass


def mix_column():
    pass


def add_roundkey(data, key):
    data = data.reshape(4, 4)
    rkey = rkey.reshape(4, 4)
    return data ^ rkey

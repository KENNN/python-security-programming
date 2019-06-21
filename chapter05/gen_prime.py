#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import random


def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, n):
        if math.sqrt(n) < i:
            return True
        elif n % i == 0:
            return False


def run():
    p, q = (0, 0)
    while (p == q) or not is_prime(p) or not is_prime(q):
        p = random.randint(10 ** 5, 10**6)
        q = random.randint(10 ** 5, 10**6)

    print('p: {}'.format(p))
    print('q: {}'.format(q))


def main():
    run()


if __name__ == '__main__':
    main()

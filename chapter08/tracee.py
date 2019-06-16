#!/usr/bin/python
# -*- coding: utf-8 -*-


def run():
    with open('/etc/hosts', 'rb') as f:
        data = f.read()
        print(data.decode())


def main():
    run()


if __name__ == '__main__':
    main()

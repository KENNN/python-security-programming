#!/usr/bin/python
# -*- coding: utf-8 -*-


def run():
    with open('/etc/hosts', 'r') as f:
        data = f.read()
        print(data)


def main():
    run()


if __name__ == '__main__':
    main()

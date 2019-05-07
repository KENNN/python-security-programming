#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route
from bottle import run
from bottle import request


@route('/')
def hello(user=''):
    username = request.query.get('user')
    username = '' if username is None else username
    html = '<h2> Hello {} </h2>'.format(username)
    return html


def main():
    run(host='localhost', port=8080, debug=True)


if __name__ == '__main__':
    main()

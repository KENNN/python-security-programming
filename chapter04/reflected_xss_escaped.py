#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route
from bottle import run
from bottle import request
import html


@route('/')
def hello(user=''):
    username = request.query.get('user')
    username = '' if username is None else username
    username = html.escape(username)

    body = '<h2> Hello {} </h2>'.format(username)
    return body


def main():
    run(host='localhost', port=8080, debug=True)


if __name__ == '__main__':
    main()

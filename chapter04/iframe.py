#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route
from bottle import run


@route('/')
def hello():
    target_url = 'http://localhost:8000'
    html = '<h2> attacker side web site </h2>'
    html += '<iframe src="{}"></iframe>'.format(target_url)
    return html


def main():
    run(host='localhost', port=8888, debug=True)


if __name__ == '__main__':
    main()

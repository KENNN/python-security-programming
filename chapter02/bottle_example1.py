#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route
from bottle import run


if __name__ == "__main__":
    @route('/hello')
    def index():
        return '<h1>Hello</h1>'

    run(host='localhost', port=8080)
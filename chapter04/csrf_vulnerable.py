#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route
from bottle import run
from bottle import request
from bottle import response
from bottle import redirect
from bottle import get
import os


USER_ID = 'user1'
os.environ['PASSWORD'] = '123456'


def is_logged_in():
    cookie = request.get_cookie('sessionid', secret='password')
    return False if cookie is None else True


def authenticate(user_id, password):
    if user_id == USER_ID and password == os.environ['PASSWORD']:
        return True
    else:
        return False


@route('/')
def index():
    html = '<h2> CSRF demo </h2>'
    if isloggedin():
        username = request.cookies('sessionid', secret='password')
        return html + 'Hello {}'.format(username)
    else:
        return html + 'You must login <a href="login"> here.</a>'


def main():
    run(host='localhost', port=8000, debug=True)


if __name__ == '__main__':
    main()

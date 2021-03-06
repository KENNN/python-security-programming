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
    if is_logged_in():
        username = request.get_cookie('sessionid', secret='password')
        html += 'Hello {}'.format(username)
        html += '<form action="/changepassword" method="POST">'
        html += 'Change password: <input type="text" name="password" />'
        html += '<input type="submit" value="update" />'
        html += '</form>'
        return html
    else:
        return html + 'You must login <a href="login"> here.</a>'


@route('/changepassword', method='POST')
def change_password():
    referer = request.headers.get('Referer')
    if referer != 'http://localhost:8000/':
        return 'The value of Referer is invalid.'
    if is_logged_in():
        new_password = request.forms.get('password')
        os.environ['PASSWORD'] = new_password
        return redirect('login')
    else:
        html = 'You must login <a href="login"> here.</a>'
        return html


@get('/login')
def login():
    html = '<h2> CSRF demo </h2>'
    html += "<form action='/login' method='POST'>"
    html += "User ID: <input type='text' name='user_id' /><br>"
    html += "Password: <input type='password' name='password' /><br>"
    html += "<input type='submit' name='register' value='login' />"
    html += "</form>"
    return html


@route('/login', method='POST')
def do_login():
    user_id = request.forms.get('user_id')
    password = request.forms.get('password')
    if authenticate(user_id, password):
        response.set_cookie('sessionid', user_id, secret='password')
        return redirect('/')
    else:
        return '<h2> CSRF demo </h2> Login failed.'


def main():
    run(host='localhost', port=8000, debug=True)


if __name__ == '__main__':
    main()

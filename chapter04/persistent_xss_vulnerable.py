#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route
from bottle import run
from bottle import request
from bottle import redirect
import sqlite3


db_name = 'tasklist.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()


def get_tasklist():
    sql_query = 'SELECT * FROM tasklist'
    result = cursor.execute(sql_query)

    html = '<table border="1">'
    for row in result:
        html += '<tr><td>'
        html += row[0]
        html += '</td><td>'
        html += row[1]
        html += '</td></tr>'
    html += '</table>'
    return html


@route('/')
def hello(user=''):
    tasks = get_tasklist()
    html = "<h2>Persistent XSS Demo</h2>"
    html += "<form action='./' method='POST'>"
    html += "task: <input type='text' name='name' /><br>"
    html += "content: <input type='text' name='detail' /><br>"
    html += "<input type='submit' name='register' value='register' />"
    html += "</form>"
    html += tasks
    return html


@route('/', method='POST')
def register():
    name = request.forms.get('name')
    detail = request.forms.get('detail')

    sql_query = 'INSERT INTO tasklist values(?, ?)'
    cursor.execute(sql_query, (name, detail))
    conn.commit()

    return redirect('/')


def main():
    run(host='localhost', port=8787, debug=True)


if __name__ == '__main__':
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os

if __name__ == '__main__':
    url = 'http://localhost:8000'
    response = None

    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Connection error was raised')
    else:
        print(response.text)
    finally:
        print('exit.')

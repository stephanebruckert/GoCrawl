#!/usr/bin/python

import requests
from pyquery import PyQuery


def stringified_page(url):
    '''
    Request a webpage
    '''
    r = requests.get(url)

    if r.status_code == 200:
        return str(PyQuery(r.text))
    else:
        raise Exception(r.status_code)

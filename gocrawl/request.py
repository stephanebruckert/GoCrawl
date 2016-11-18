#!/usr/bin/python

import requests
from pyquery import PyQuery
import json


def stringified_page(url):
    try:
        r = requests.get(url)
    except Exception, e:
        print

    if r.status_code == 200:
        return str(PyQuery(r.text))
    else:
        raise Exception(r.status_code)

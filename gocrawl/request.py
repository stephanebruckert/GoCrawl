#!/usr/bin/python

import requests
from pyquery import PyQuery
import json


def stringified_page(url):
    r = requests.get(url)

    if r.status_code == 200:
        return str(PyQuery(r.text))
    else:
        raise Exception(r.status_code)

#!/usr/bin/python

from queuer import Queuer
from parser import Parser
import request
import report


def core(entry_point, should_print):
    '''
    Loop over pages of the entry point domain
    and retrieve their assets
    '''
    # Initiate with a first link
    queuer = Queuer(entry_point, should_print)
    Parser.set_domain_name(entry_point)

    while True:
        current_url = queuer.next_unvisited()
        if current_url is None:
            break
        try:
            results = read_page(current_url)
        except Exception, code:
            queuer.add_invalid(current_url, code)
            continue
        queuer.add(results, current_url)

    report.output_json(queuer.results)


def read_page(url):
    '''
    Get page content before finding links and assets
    '''
    # Request the page
    p = request.stringified_page(url.strip())

    # Get normalized links
    return Parser(url).search(p)

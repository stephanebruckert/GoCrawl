#!/usr/bin/python

from queuer import Queuer
from parse import Parser
import request
import report


def core(entry_point):
    # Initiate with a first link
    queuer = Queuer(entry_point)
    Parser.set_domain_name(entry_point)

    while True:
        current_url = queuer.next_unvisited()
        if current_url is None:
            break
        try:
            (page_links, image_assets, js_assets,
                css_assets) = crawl(current_url)
        except Exception, e:
            queuer.add_invalid(current_url)
            continue
        queuer.add(page_links, current_url,
                   image_assets, js_assets, css_assets)

    print 'Done.'
    report.output_json(queuer.results)
    # TODO Save results in file


def crawl(url):
    # Request the page
    p = request.stringified_page(url.strip())

    # Get normalized links
    return Parser(url).search(p)

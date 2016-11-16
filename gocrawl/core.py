#!/usr/bin/python

from queuer import Queuer
from parse import Parser
import request


def main():
    entry_point = "http://bbc.co.uk"

    # Initiate with a first link
    queuer = Queuer(entry_point)
    Parser.set_domain_name(entry_point)

    while True:
        current_url = queuer.next_unvisited()
        if current_url is None:
            break
        try:
            page_links = crawl(current_url)
        except Exception, e:
            queuer.add_unvalid(current_url)
            continue
        queuer.add(page_links, current_url)

    print 'done'
    # report(queuer.visited_links())


def crawl(url):
    # Request the page
    page = request.stringified_page(url.strip())
    print page
    # Get normalized links
    return Parser(url).links_from_page(page)


if __name__ == "__main__":
    main()

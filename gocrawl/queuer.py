#!/usr/bin/python

import Queue


class Queuer(object):

    def __init__(self, entry_point, should_print):
        print 'Crawling %s...' % entry_point

        self.unvisited = Queue.Queue()
        self.unvisited.put(entry_point.decode('utf-8'))
        self.visited = []
        self.invalid = []
        self.results = []
        self.should_print = should_print

    '''
    The next page to visit in the waiting list
    '''
    def next_unvisited(self):
        if not self.unvisited.empty():
            return self.unvisited.get()

    '''
    Populate a visited page with its assets,
    adds linked pages to waiting list,
    '''
    def add(self, results, current_url):
        assets = {}
        for asset in results['assets']:
            assets[asset] = results['assets'][asset]

        current_page_data = {
            'url': current_url,
            'assets': assets
        }

        self.results.append(current_page_data)
        self.visited.append(current_url)

        for link in results['next']['url']:
            if link not in self.unvisited.queue and link not in self.visited:
                self.unvisited.put(link)

        self.print_status(current_url)

    '''
    Save a list of corrupt pages
    '''
    def add_invalid(self, invalid_url, status_code):
        self.invalid.append(invalid_url)
        self.print_status(invalid_url, status_code)

    '''
    Status after visiting current page
    '''
    def print_status(self, current_url, status_code=None):
        if not self.should_print:
            return
        invalid = 'Invalid: {0}, because {1}'.format(
            str(len(self.invalid)), status_code) if status_code else ''

        print "{0:60} Visited: {1:6} Remaining: {2:8} {3}".format(
            current_url,
            str(len(self.visited)),
            str(self.unvisited.qsize()),
            invalid
        )

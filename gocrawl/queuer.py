#!/usr/bin/python

import Queue
import json


class Queuer(object):

    # TODO current_url should be instance attribute
    # TODO all lists should be class attributes
    def __init__(self, entry_point):
        self.unvisited = Queue.Queue()
        self.unvisited.put(entry_point.decode('utf-8'))
        self.visited = []
        self.invalid = []
        self.results = []

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
    def add(self, next_page_links, current_url, image_assets, js_assets,
            css_assets):
        current_page_data = {
            'url': current_url,
            'assets': {
                'images': image_assets,
                'js': js_assets,
                'css': css_assets
            }
        }
        self.results.append(current_page_data)
        self.visited.append(current_url)

        for link in next_page_links:
            if link not in self.unvisited.queue and link not in self.visited:
                self.unvisited.put(link)

        self.print_status(current_url)

    '''
    Save a list of corrupt pages
    '''
    def add_invalid(self, invalid_url):
        self.invalid.append(invalid_url)

    '''
    Status after visiting current page
    '''
    def print_status(self, current_url):
        print current_url \
            + ' Unvisited: ' + str(self.unvisited.qsize()) \
            + ' Visited: ' + str(len(self.visited))

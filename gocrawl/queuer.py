#!/usr/bin/python

import Queue
import json

class Queuer(object):

    def __init__(self, entry_point):
        self.unvisited = Queue.Queue()
        self.unvisited.put(entry_point.decode('utf-8'))
        self.visited = []
        self.unvalid = []

    def next_unvisited(self):
        if not self.unvisited.empty():
            return self.unvisited.get()

    def add(self, next_page_links, current_url, image_assets, js_assets):
        current_page_data = {
            'url': current_url,
            'assets': {
                'images': image_assets,
                'js': js_assets
            }
        }
        self.visited.append(current_page_data)

        for link in next_page_links:
            if link not in self.unvisited.queue and link not in self.visited:
                self.unvisited.put(link)

        print json.dumps(current_page_data, indent=2) \
            + ' Unvisited: ' + str(self.unvisited.qsize()) \
            + ' Visited: ' + str(len(self.visited))

        # - Will divide them in 2 categories
        #   - other pages
        #   - assets (and associate them with the current page)
        # - Add them to lists
        #   - Check if not already visited or not already queued, otherwise
        #           add to queue)
        # - Create a visited_page object, add its assets
        # - Remove from queue
        # - Add to visited list

    def add_unvalid(self, unvalid_url):
        self.unvalid.append(unvalid_url)

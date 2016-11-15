#!/usr/bin/python

import Queue


class Queuer(object):

    def __init__(self, entry_point):
        self.unvisited = Queue.Queue()
        self.unvisited.put(entry_point.decode('utf-8'))
        self.visited = []

    def next_unvisited(self):
        if not self.unvisited.empty():
            next = self.unvisited.get()
            return next

    def add(self, page_links, current_url):
        self.visited.append(current_url)

        for link in page_links:
            if link not in self.unvisited.queue and link not in self.visited:
                self.unvisited.put(link)

        print current_url \
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

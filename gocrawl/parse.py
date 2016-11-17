#!/usr/bin/python

from bs4 import BeautifulSoup
import urlparse
from pprint import pprint


class Parser(object):

    def __init__(self, current_url):
        self.url = current_url

    @classmethod
    def set_domain_name(cls, entry_point):
        cls.domain_name = urlparse.urlparse(entry_point).hostname

    '''
    Retrieving any links to pages of the same domain
    '''
    def search(self, page_str):
        element = BeautifulSoup(page_str, 'html.parser')

        # create rules
        pages = element.find_all('a', href=True)
        images = element.find_all('img', src=True)
        js = element.find_all('script', src=True)
        css = element.find_all('link', type="text/css")

        return (self.filter(pages, 'href'),
                self.filter(images, 'src'),
                self.filter(js, 'src'),
                self.filter(css, 'href'))

    def filter(self, links, type):
        hrefs = [self.normalize_href(l[type]) for l in links]
        hrefs = list(set(hrefs))  # Remove duplicates
        return filter(lambda href: href is not None, hrefs)

    '''
    Normalize urls and keep only those from the current domain
    '''
    def normalize_href(self, href):
        if self.is_href_acceptable(href):
            normalized_href = urlparse.urljoin(self.url, href)
            if (self.domain_name in normalized_href):
                return normalized_href

    def is_href_acceptable(self, href):  # self looks useless
        return (len(href) > 0 and
                href[0] != '#' and not  # TODO we need to remove anchors
                href.startswith("mailto"))

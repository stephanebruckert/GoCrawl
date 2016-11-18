#!/usr/bin/python

from bs4 import BeautifulSoup
import urlparse


class Parser(object):
    rules = {
                'next': {
                    'url':    [['a', 'href']]
                },
                'assets': {
                    'images': [['img', 'src']],
                    'css':    [['link', 'href']],
                    'js':     [['script', 'src']]
                }
            }

    def __init__(self, current_url):
        self.url = current_url

    '''
    The parser needs to know which domain to refer to
    '''
    @classmethod
    def set_domain_name(cls, entry_point):
        cls.domain_name = urlparse.urlparse(entry_point).hostname

    '''
    Retrieving any links to pages of the same domain
    '''
    def search(self, page_str):
        element = BeautifulSoup(page_str, 'html.parser')

        results = {}
        for cat in self.rules:
            results[cat] = {}
            for el_type in self.rules[cat]:
                results[cat][el_type] = []
                for rule in self.rules[cat][el_type]:
                    tags = element.find_all(rule[0], **{rule[1]: True})
                    results[cat][el_type].extend(self.filter(tags, rule[1]))
        return results

    '''
    Clean HTML tags, normalize HREF, and remove duplicates from list of links
    '''
    def filter(self, tags, type):
        hrefs = [self.normalize_href(t[type]) for t in tags]
        hrefs_without_duplicates = list(set(hrefs))
        return filter(lambda href: href is not None, hrefs_without_duplicates)

    '''
    Normalize urls and keep only those from the current domain
    '''
    def normalize_href(self, href):
        accepted_href = self.useful_href(href)
        if accepted_href:
            normalized_href = urlparse.urljoin(self.url, accepted_href)
            # exclude google.com/domain-i-am-crawling.com
            uri_object = urlparse.urlparse(normalized_href)
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=uri_object)
            if (self.domain_name in domain):
                return normalized_href

    '''
    href can be useful, modified to be useful, or lost cause
    '''
    @staticmethod
    def useful_href(href):
        if (len(href) > 0 and
                href[0] != '#' and not
                href.startswith("mailto")):
            try:
                return href[:href.index('#')]  # remove the URL anchor
            except ValueError, e:
                return href
        else:
            False

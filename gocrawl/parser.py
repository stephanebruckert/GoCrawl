#!/usr/bin/python

from bs4 import BeautifulSoup
import urlparse


class Parser(object):

    ''' Search rules for links and assets to be defined as such '''
    rules = {
                'next': {
                    'url':    [['a', 'href', True, 'href']]
                },
                'assets': {
                    'images': [['img', 'src', True, 'src']],
                    'css':    [
                                ['link', 'rel', 'stylesheet', 'href'],
                                ['link', 'type', 'text/css', 'href'],
                                ['link', 'rel', 'stylesheet/less', 'href'],
                                ['link', 'rel', 'stylesheet/css', 'href']
                              ],
                    'js':     [['script', 'src', True, 'src']]
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
    Search for contents in page according to defined rules
    '''
    def search(self, page_str):
        element = BeautifulSoup(page_str, 'html.parser')

        results = {}
        for cat in self.rules:
            results[cat] = {}
            for el_type in self.rules[cat]:
                results[cat][el_type] = []
                for rule in self.rules[cat][el_type]:
                    tags = element.find_all(rule[0], **{rule[1]: rule[2]})
                    results[cat][el_type].extend(self.filter(tags, rule[3]))
                # remove duplicates because of identical rules
                results[cat][el_type] = list(set(results[cat][el_type]))
        return results

    '''
    Clean HTML tags, normalize URIs, and remove duplicate links
    '''
    def filter(self, tags, type):
        hrefs = [self.normalize_uri(t[type]) for t in tags]
        return filter(lambda href: href is not None, hrefs)

    '''
    Normalize urls and keep only those from the current domain
    '''
    def normalize_uri(self, uri):
        accepted_uri = self.useful_uri(uri)
        if accepted_uri:
            normalized_uri = urlparse.urljoin(self.url, accepted_uri)
            # exclude google.com/domain-i-am-crawling.com
            uri_object = urlparse.urlparse(normalized_uri)
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=uri_object)
            if (self.domain_name in domain):
                return normalized_uri

    '''
    URI can be useful, modified to be useful, or lost cause
    '''
    @staticmethod
    def useful_uri(uri):
        try:
            uri.index('@')
        except ValueError:
            if (len(uri) > 0 and
                    uri[0] != '#' and not
                    uri.startswith("mailto")):
                try:
                    return uri[:uri.index('#')]  # remove the URL anchor
                except ValueError:
                    return uri

#!/usr/bin/python

from bs4 import BeautifulSoup
import urlparse


class Parser(object):

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

        # create rules
        pages = element.find_all('a', href=True)
        images = element.find_all('img', src=True)
        js = element.find_all('script', src=True)
        css = element.find_all('link', type="text/css")

        return (self.filter(pages, 'href'),
                self.filter(images, 'src'),
                self.filter(js, 'src'),
                self.filter(css, 'href'))

    '''
    Clean HTML tags, normalize HREF, and remove duplicates from list of links
    '''
    def filter(self, links, type):
        hrefs = [self.normalize_href(l[type]) for l in links]
        hrefs = list(set(hrefs))  # removes duplicates
        return filter(lambda href: href is not None, hrefs)

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

# class WebPage(object):

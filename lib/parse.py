#!/usr/bin/python

from bs4 import BeautifulSoup
import urlparse


class Parser(object):

    def __init__(self, current_url):
        self.url = current_url

    @classmethod
    def set_domain_name(cls, entry_point):
        cls.domain_name = urlparse.urlparse(entry_point).hostname

    def links_from_page(self, page_str):
        soup = BeautifulSoup(page_str, 'html.parser')
        all_links = soup.find_all('a', href=True)
        return self.get_hrefs(all_links)

    def get_hrefs(self, links):
        hrefs = [self.normalize_href(l['href']) for l in links]
        return filter(lambda href: href is not None, hrefs)

    '''
    Normalize urls and keep only those from the current domain
    '''
    def normalize_href(self, href):
        if self.is_href_acceptable(href):
            normalized_href = urlparse.urljoin(self.url, href)
            if (self.domain_name in normalized_href):
                return normalized_href

    def is_href_acceptable(self, href):
        return (len(href) > 0 and
                href[0] != '#' and not
                href.startswith("mailto"))

# -*- coding: utf-8 -*-

from gocrawl.parser import Parser

import unittest


class SearchTestSuite(unittest.TestCase):
    '''
    Retrieving any links to pages of the same domain
    '''

    def setUp(self):
        self.parser = Parser("http://wikipedia.org/foo/bar")
        self.parser.set_domain_name("http://wikipedia.org/")

    def tearDown(self):
        del self.parser

    def test(self):
        page_str = '<script src="portal/wikipedia.org" />\
                    <img src="correct_image_tag" />\
                    <link href="correct_css_tag" />\
                    <a href="http://wikipedia.org/next_page" />\
                    <link src="http://wikipedia.org/ignored_link" />\
                    <a href="http://google.com/">Wrong Domain</a>'

        res = {
                'assets': {
                    'images': [u'http://wikipedia.org/foo/correct_image_tag'],
                    'css': [u'http://wikipedia.org/foo/correct_css_tag'],
                    'js': [u'http://wikipedia.org/foo/portal/wikipedia.org']
                },
                'next': {
                    'url': [u'http://wikipedia.org/next_page']
                }
            }

        self.assertEqual(self.parser.search(page_str), res)


class UsefulHrefTestSuite(unittest.TestCase):
    '''
    href can be useful, modified to be useful, or lost cause
    '''

    def test_returns_true(self):
        self.assertTrue(
            Parser.useful_href("hello"))

    def test_starts_with_hash_returns_false(self):
        self.assertFalse(
            Parser.useful_href("#hello"))

    def test_remove_hash(self):
        self.assertEquals(
            Parser.useful_href("hello#"), "hello")

    def test_remove_after_hash(self):
        self.assertEquals(
            Parser.useful_href("hello#world"), "hello")

    def test_single_hash_returns_false(self):
        self.assertFalse(
            Parser.useful_href("#"))

    def test_mail_returns_false(self):
        self.assertFalse(
            Parser.useful_href("mailto:mail@to.com"))


class NormalizeHrefTestSuite(unittest.TestCase):
    '''
    Normalize urls and keep only those from the current domain
    '''

    def setUp(self):
        self.parser = Parser("http://wikipedia.org/foo/bar")
        self.parser.set_domain_name("http://wikipedia.org/")

    def tearDown(self):
        del self.parser

    def test_returns_true(self):
        self.assertEquals(
            self.parser.normalize_href("http://wikipedia.org/"),
            "http://wikipedia.org/")

    def test_returns_true_when_subdomain(self):
        self.assertEquals(
            self.parser.normalize_href("http://fr.wikipedia.org/"),
            "http://fr.wikipedia.org/")

    def test_wrong_domain_returns_false(self):
        self.assertFalse(
            self.parser.normalize_href("http://google.com"))

    def test_wrong_and_good_domain_returns_false(self):
        self.assertFalse(
            self.parser.normalize_href("http://google.com/wikipedia.org"))

    def test_anchor_returns_false(self):
        self.assertFalse(
            self.parser.normalize_href("#"))

    def test_returns_false(self):
        self.assertEquals(
            self.parser.normalize_href("/world#"),
            "http://wikipedia.org/foo/world")

    def test_returns_false(self):
        self.assertEquals(
            self.parser.normalize_href("../hello/world#"),
            "http://wikipedia.org/hello/world")

if __name__ == '__main__':
    unittest.main()

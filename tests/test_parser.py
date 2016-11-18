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
            Parser.useful_uri("hello"))

    def test_starts_with_hash_returns_false(self):
        self.assertFalse(
            Parser.useful_uri("#hello"))

    def test_remove_hash(self):
        self.assertEquals(
            Parser.useful_uri("hello#"), "hello")

    def test_remove_after_hash(self):
        self.assertEquals(
            Parser.useful_uri("hello#world"), "hello")

    def test_single_hash_returns_false(self):
        self.assertFalse(
            Parser.useful_uri("#"))

    def test_mail_returns_false(self):
        self.assertFalse(
            Parser.useful_uri("mailto:mail@to.com"))


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
            self.parser.normalize_uri("http://wikipedia.org/"),
            "http://wikipedia.org/")

    def test_returns_true_when_subdomain(self):
        self.assertEquals(
            self.parser.normalize_uri("http://fr.wikipedia.org/"),
            "http://fr.wikipedia.org/")

    def test_wrong_domain_returns_false(self):
        self.assertFalse(
            self.parser.normalize_uri("http://google.com"))

    def test_wrong_and_good_domain_returns_false(self):
        self.assertFalse(
            self.parser.normalize_uri("http://google.com/wikipedia.org"))

    def test_anchor_returns_false(self):
        self.assertFalse(
            self.parser.normalize_uri("#"))

    def test_returns_false(self):
        self.assertEquals(
            self.parser.normalize_uri("/world#"),
            "http://wikipedia.org/foo/world")

    def test_returns_false(self):
        self.assertEquals(
            self.parser.normalize_uri("../hello/world#"),
            "http://wikipedia.org/hello/world")

if __name__ == '__main__':
    unittest.main()

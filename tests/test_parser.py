# -*- coding: utf-8 -*-

from gocrawl.parse import Parser

import unittest


class UsefulHrefTestSuite(unittest.TestCase):
    """Basic test cases."""

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
    """Basic test cases."""

    def setUp(self):
        self.parser = Parser("http://wikipedia.org/foo/bar")
        self.parser.set_domain_name("http://wikipedia.org/")

    def tearDown(self):
        del self.parser

    def test_returns_true(self):
        self.assertEquals(
            self.parser.normalize_href("http://wikipedia.org/"),
            "http://wikipedia.org/")

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

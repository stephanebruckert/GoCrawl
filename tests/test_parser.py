# -*- coding: utf-8 -*-

from gocrawl.parse import Parser

import unittest


class IsHrefAcceptableTestSuite(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        self.parser = Parser("http://wikipedia.org")

    def tearDown(self):
        del self.parser

    def test_valid_href_returns_true(self):
        self.assertTrue(
            self.parser.is_href_acceptable("hello"))

    def test_is_href_acceptable_returns_false_when_starts_with_hashtag(self):
        self.assertFalse(
            self.parser.is_href_acceptable("#hello"))

    def test_is_href_acceptable_returns_false_when_empty_string(self):
        self.assertFalse(
            self.parser.is_href_acceptable(""))

    def test_is_href_acceptable_returns_false_when_mailto(self):
        self.assertFalse(
            self.parser.is_href_acceptable("mailto:mail@to.com"))

if __name__ == '__main__':
    unittest.main()

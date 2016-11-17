# -*- coding: utf-8 -*-

from gocrawl.parse import Parser

import unittest


class UsefulHrefTestSuite(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        self.parser = Parser("http://wikipedia.org")

    def tearDown(self):
        del self.parser

    def test_returns_true(self):
        self.assertTrue(
            Parser.useful_href("hello"))

    def test_starts_with_hash_returns_false(self):
        self.assertFalse(
            Parser.useful_href("#hello"))

    def test_remove_hash(self):
        self.assertFalse(
            Parser.useful_href("hello#"))

    def test_remove_after_hash(self):
        self.assertEquals(
            Parser.useful_href("hello#world"), "hello")

    def test_single_hash_returns_false(self):
        self.assertFalse(
            Parser.useful_href("#"))

    def test_mail_returns_false(self):
        self.assertFalse(
            Parser.useful_href("mailto:mail@to.com"))

if __name__ == '__main__':
    unittest.main()

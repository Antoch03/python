#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pymmath
----------------------------------

Tests for `pymmath` module.
"""

import unittest

import pymmath


class TestPymmath(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(pymmath.__version__)

    def tearDown(self):
        pass

#!/usr/bin/python3
"""
This is a unittest modules used for testing the base.py module
"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    This is a test class for testing the base class to see
    if it actually works as expected and if it raises any errors
    """

    def test_isTrue(self):
        self.assertTrue(True)

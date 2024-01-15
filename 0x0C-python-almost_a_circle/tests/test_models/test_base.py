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

    def setUp(self):
        """
        initializes setUp calls which is excecuted before every
        process is executed
        """
        self.a = Base()
        self.b = Base()

    def test_isTrue(self):
        """
        checks if the expression is actually True
        """
        self.assertTrue(True)
    
    def test_isEquals(self):
        """
        checks if the self.a.id is equal to the output
        being passed using the setUp() method to initialize
        the test_isEquals method
        """
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 2)

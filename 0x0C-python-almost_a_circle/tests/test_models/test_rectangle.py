#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    
    def setUp(self):
        """
        setUp function for instansiating other methods
        """
        self.a = Rectangle(12, 54)
        self.b = Rectangle(23, 15)
    
    def test_isEquals(self):
        """
        checks if the output of the attribute is equals to
        the expected output
        """
        self.assertEqual(self.a.height, 54)
        self.assertEqual(self.a.width, 12)
        self.assertEqual(self.b.width, 23)
        self.assertEqual(self.b.height, 15)
    
    def test_isTrue(self):
        """ checks if its true"""
        self.assertTrue(self.a)
        self.assertTrue(self.b)
    
    @unittest.expectedFailure
    def test_error(self):
        """
        Tells the runner that when executed it would see an error
        """
        self.assertEqual(self.a.__height, 54)
        self.assertEqual(self.b.__height, 15)
        self.assertEqual(self.a.__height, 12)
        self.assertEqual(self.b.__width, 23)

    def test_isNot(self):
        """
        checks is both are the same
        """
        self.assertIsNot(self.a, self.b)
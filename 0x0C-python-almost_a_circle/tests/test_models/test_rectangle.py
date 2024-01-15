#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    This is a test class for testing the base class to see
    if it actually works as expected and if it raises any errors
    """

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
        self.assertIsNot(self.b, self.a)

    def test_isinstance(self):
        """
        Checks if the instance is correct
        """
        self.assertIsNotNone(self.a, int)
        self.assertIsNotNone(self.b, int)
        self.assertIsNotNone(self.b, str)
        self.assertIsNotNone(self.a, str)
        self.assertIsNotNone(self.a, tuple)
        self.assertIsNotNone(self.a, tuple)

    def test_isNotNone(self):
        """
        Checks if its not none
        """
        law_test = Rectangle(12, 7)
        self.assertIsNotNone(law_test)

    def test_error_raised(self):
        with self.assertRaises(ValueError):
            caseA = Rectangle(14, 54, -1, 0)
        with self.assertRaises(ValueError):
            caseA = Rectangle(14, 54, 2, -1)
        with self.assertRaises(ValueError):
            caseA = Rectangle(14, 32, 12, -100)
        with self.assertRaises(ValueError):
            caseA = Rectangle(14, 54, -1, -1)

    def test_missing_arguments(self):
        """
        Test for if no parameter was passed as an object
        """
        with self.assertRaises(TypeError):
            CaseA = Rectangle()

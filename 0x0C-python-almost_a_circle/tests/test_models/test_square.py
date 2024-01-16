#!/usr/bin/python3

from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.starA = Square(21)
        self.starB = Square(0)

    def test_isEqual_to(self):
        self.assertEqual(self.starA.width, 21)
        self.assertEqual(self.starB.height, 0)

    def test_isTrue(self):
        self.assertTrue(self.starA)
        self.assertTrue(self.starB)

    def test_is_square(self):
        self.assertIsNot(self.starA.id, self.starB.id)
        self.assertIsNot(self.starA.height, self.starB.height)

    def test_is_not_same_square(self):
        self.assertIsNot(self.starA, self.starB)
        self.assertIsNot(self.starA.id, self.starB.id)

    def test_is_greater(self):
        self.assertGreater(self.starA.width, self.starB.width)

    def test_missing_arguments(self):
        """
        Test for if no parameter was passed as an object
        """
        with self.assertRaises(TypeError):
            CaseA = Square()

    def test_expect_error(self):
        with self.assertRaises(TypeError):
            self.starA in self.starB

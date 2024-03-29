#!/usr/bin/python3
"""
Write a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    Parent class with several functionalities
    as well as methods
    """

    def area(self):
        """
        that raises an Exception with the
        message area() is not implemented

        Raises:
            Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        that validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError
        exception with the message <name> must be greater than 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")

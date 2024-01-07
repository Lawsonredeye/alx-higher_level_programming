#!/usr/bin/python3
"""
Module with the addition function that
just adds two values together (a and b)
also returns the value of the sum of a and b
"""


def add_integer(a, b=98):
    """
    function that adds two integer together

    Args:
        a (int): integer or float parameter
        b (int): integer or float parameter

    Raises:
        TypeError: if either a or b is not an integer or a float
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a + b)

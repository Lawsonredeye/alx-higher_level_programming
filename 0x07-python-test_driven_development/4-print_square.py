#!/usr/bin/python3
"""
module which has a printing function
Does not return anything
"""


def print_square(size):
    """
    function that prints a square with the character #
    Args:
        size: must be an integer to specified the size

    Raises:
        TypeError: raises an exception
        ValueError: raises an exception
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#"*size)

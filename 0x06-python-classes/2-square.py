#!/usr/bin/python3
"""
class Square that defines a square by: (based on 1-square.py)
"""

class Square:
    """
    class that just pass when called and accessed
    Attributes:
        size
    """

    def __init__(self, size=0):
        """
        using the __init__ method to initialize the code
        Attributes:
            size: just the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
     

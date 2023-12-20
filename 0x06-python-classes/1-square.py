#!/usr/bin/python3
"""
class Square that defines a square by: (based on 0-square.py)
"""


class Square:
    """class that just pass when called and accessed
        Attributes:
            size
    """
    def __init__(self, size):
        """
        using the __init__ method to initialize the code
        
        Attribute:
            size: just the size of the square
        """
        self.__size = size

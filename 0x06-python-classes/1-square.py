#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""class Square that defines a square by: (based on 0-square.py)
"""


class Square:
    """class that just pass when called and accessed
        Attributes:
        No Attributes
    """
    
    def __init__(self, size):
        """using the __init__ method to initialize the code
        
        Args:
            size (int): just the size of the square on the private mode
        """
        self.__size = size

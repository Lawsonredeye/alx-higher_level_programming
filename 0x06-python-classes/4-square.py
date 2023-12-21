#!/usr/bin/python3
"""
class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    """
    class that just pass when called and accessed
    
    Attributes:
        __size: size of the defined area
    """

    def __init__(self, size=0):
        """
        using the __init__ method to initialize the code
        
        Attributes:
            size: just the size of the square
        
        Raises:
            TypeError: If something other than an int is passed
            ValueError: If the size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """
        returns the current square area
        Attributes:
            No attributes assigned
        """
        return self.__size * self.__size
    
    @property
    def size(self):
        """
        gets the size of the __size
        
        Args:
            __size: size to be returned
        Return:
            self.__size
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        sets the size to get the value

        Args:
            __size (int): integer
            value: sets the self.__size to itself
        
        Raises:
            TypeError: If something other than an int is passed
            ValueError: If the size is less than zero
        """
    
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

#!/usr/bin/python3
"""
empty class Rectangle that defines a rectangle
"""


class Rectangle:

    """Class that defines a rectangle

    It has both setters and getters using the @property decorators
    as with som returning value

    Args:
        width (int): width of the triangle and it should be greater than 0
        height (int): height and its greater than 0

    Attributes:
        width (int): width of the triangle and it should be greater than 0
        height (int): height and its greater than 0
    """

    def __init__(self, width=0, height=0):
        """Initializes the instance of the class Rectangle
        based on width and height

        Args:
            width: parameter for width
            height: parameter for the rect height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        int: Getter that returns the width of a rectangle

        Return:
            width(int): the setted value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """int: sets the width using the value parameter

        Raise:
            TypeError: if value isnt an int
            ValueError: if value is less than or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        int: Getter that returns the width of a rectangle

        Return:
            height(int): the setted value of width
        """
        return self.__height

    @height.setter
    def height(self, value):
        """int: sets the height using the value parameter

        Raise:
            TypeError: if value isnt an int
            ValueError: if value is less than or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

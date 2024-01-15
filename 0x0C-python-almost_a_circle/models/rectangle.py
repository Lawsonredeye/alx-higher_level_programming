#!/usr/bin/python3
"""
Module which depends on the base.py module to be able to carry out its
operation and also imports methods from the base.py 
"""


from models.base import Base

class Rectangle(Base):
    """
    Inherits values from base.py to have access to its id and has
    several getters and setters for setting and retriving the height,
    width, x, y and id

    Args:
        width (int): values for the width of the rectangle
        height (int): values for height of the rectangle
        x (int): 0 (Default) optional if not passed
        y (int): 0 (Default) optional if not passed
        id (int): None (Default)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instanciating the Rectangle class and it takes 2 important
        parameters and 3 optional parameters

        Args:
            width (int): values for the width of the rectangle
            height (int): values for height of the rectangle
            x (int): 0 (Default) optional if not passed
            y (int): 0 (Default) optional if not passed
            id (int): None (Default)
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Public getter that retrives and return the actual
        width
        """
        return self.__width

    @property
    def height(self):
        """
        Public getter that retrives and return the actual
        height
        """
        return self.__height

    @property
    def x(self):
        """
        Public getter that retrives and return the actual
        x
        """
        return self.__x

    @property
    def y(self):
        """
        Public getter that retrives and return the actual
        width
        """
        return self.__y

    @width.setter
    def width(self, width):
        """
        sets the width from the default value
        or from its previous value to a new value
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be an integer")
        self.__width = width

    @height.setter
    def height(self, width):
        """
        Resets the height from the default value
        or from its previous value to a new value
        """
        self.__height = width

    @y.setter
    def y(self, width):
        """
        Resets the y from the default value
        or from its previous value to a new value
        """
        self.__y = width

    @x.setter
    def x(self, width):
        """
        Change the value of x from the default value
        or from its previous value to a new value
        """
        self.__y = width

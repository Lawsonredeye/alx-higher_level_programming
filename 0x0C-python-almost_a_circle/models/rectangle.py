#!/usr/bin/python3

from base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
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
        self.__width = width
    
    @height.setter
    def width(self, width):
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
        self.__width = width
    
    @x.setter
    def x(self, width):
        """
        Change the value of x from the default value
        or from its previous value to a new value
        """
        self.__width = width



    
    
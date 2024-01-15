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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
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

        Args:
            width (int): recieves an integer as a parameter

        Raises:
            TypeError: if the width is not an integer
            ValueError: if the width is less than ZERO
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """
        Resets the height from the default value
        or from its previous value to a new value

        Args:
            height (int): recieves an integer as a parameter

        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than ZERO
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be > 0")
            self.__height = height

    @y.setter
    def y(self, y):
        """
        Resets the y from the default value
        or from its previous value to a new value

        Args:
            y (int): recieves an integer as a parameter

        Raises:
            ValueError: if the width is less than ZERO
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @x.setter
    def x(self, x):
        """
        Change the value of x from the default value
        or from its previous value to a new value

        Args:
            y (int): recieves an integer as a parameter

        Raises:
            ValueError: if the width is less than ZERO
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    def area(self):
        """
        This function just returns the area of a rectangle by
        multiplying height * width and returning the multiplied value
        """
        return self.__height * self.__width

    def display(self):
        """
        Prints the rectangle based on the length of the height
        and the width size
        """
        if self.__x != 0:
            for j in range(self.__x):
                print()
        rect = "#"*self.__width
        for i in range(self.__height):
            print(rect.rjust(self.__y + self.__width))

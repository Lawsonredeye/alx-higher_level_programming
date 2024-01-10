#!/usr/bin/python3
"""
Write a class BaseGeometry (based on 7-base_geometry.py).
"""


class BaseGeometry:
    """
    Parent class with several functionalities
    as well as methods
    """

    def area(self):
        """
        that raises an Exception with the
        message area() is not implemented

        Raises:
            Exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates if two objects being passed as parameters are same

        Raises:
            ValueError
            TypeError
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits the parent class BaseGeomerty
    also has access to the integer_validator
    """
    def __init__(self, width, height):
        """
        used to initialize the child class

        Args:
            width: width of the class rectangle
            height: height of the class rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns width * height
        """
        return self.__height * self.__width

    def __str__(self):
        """
        returns what was executed
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    child class to the parent class Rectangle
    """

    def __init__(self, size):
        """
        initialization mode for the object using the self
        as well as the size

        Args:
            size: used to initialize the integer
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        returns width * height
        """
        print(self.__size * self.__size)

    def __str__(self):
        """
        returns what was executed
        """
        return f"[Rectangle] {self.__size}/{self.__size}"

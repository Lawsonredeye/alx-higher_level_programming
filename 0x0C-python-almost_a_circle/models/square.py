#!/usr/bin/python3
"""
This module contains a  class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A child class which depends on the Rectangle class for its
    instances and has a new argument size which replaces the width
    and height as the height and width of a rectangle is the same

    Args:
        size (int): must be an integer and is used by both width and height
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes the Square with a new argument SIZE
        """
        super().__init__(width=size, height=size, x=0, y=0)

    def __str__(self):
        """
        Returns a string in a specific when being called or printed out
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

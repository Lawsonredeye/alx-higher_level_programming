#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            if isinstance(size, int):
                raise TypeError("size must be an integer")
        except (TypeError):
            print("size must be an integer")
        self.__size = size
        
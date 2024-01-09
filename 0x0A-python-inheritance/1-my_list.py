#!/usr/bin/python3
"""
Module that just that holds a class that
recieves a class as an object
"""


class MyList(list):
    """
    class MyList that inherits from list

    Args:
        list: must be a class
    """
    def __init__(self):
        """
        initialize using the super().__init__() function
        """
        super().__init__()
    
    def print_sorted(self):
        """
        prints the sorted value to the stdout output and
        it doesnt affect the original list
        """
        self.value = self.copy()
        self.value.sort()
        print(self.value)
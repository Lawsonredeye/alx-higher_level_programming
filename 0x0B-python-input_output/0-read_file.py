#!/usr/bin/python3
"""
This module contains a function that reads a file
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8)
    and prints it to stdout using the print function

    Args:
        filename (str): a string which is a path to a file
    """
    with open(filename, "r") as f:
        read_data = f.read()
        print(read_data)

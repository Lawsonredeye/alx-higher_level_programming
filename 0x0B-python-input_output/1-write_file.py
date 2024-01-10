#!/usr/bin/python3
"""
Module that has a function to write from an existing file and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    This function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str): th
    """
    with open(filename, "w", encoding="UTF-8") as f:
        write_data = f.write(text)
        return write_data

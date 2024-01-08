#!/usr/bin/python3
"""
This module contains a function that breaks a string based on the input
if it encounters a '.', '?' and ':' it prints a newline
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        str: takes in text as a string

    Raises:
        TypeError: if the parameter passed is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i == "." or i == "?" or i == ":":
            print("\n")
        else:
            print(i, end="")

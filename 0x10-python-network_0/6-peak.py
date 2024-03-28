#!/usr/bin/python3
"""
Peak finder module that gets the peak number of a list
By turing the list to a set and returning the last element
"""


def find_peak(list_of_integers):
    """
    Function that gets the peak value from a list
    : param: list - The list to be traversed and sorted
    """
    if list_of_integers == []:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]

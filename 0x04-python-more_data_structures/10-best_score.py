#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key = 0
    key2 = None
    for i in a_dictionary:
        if a_dictionary[i] > key:
            key = a_dictionary[i]
            key2 = i
    return key2

#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    tups = (len(sentence), sentence[0])
    return tups

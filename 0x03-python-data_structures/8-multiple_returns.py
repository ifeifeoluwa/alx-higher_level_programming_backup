#!/usr/bin/python3

"""
    returns a tuple with the length of a string and its first character."""


def multiple_returns(sentence):
    strtuple = ()
    if sentence == "":
        strtuple = 0, "None"
    else:
        strtuple = len(sentence), sentence[0]
    return strtuple

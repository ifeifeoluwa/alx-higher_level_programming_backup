#!/usr/bin/python3

"""
    returns a tuple with the length of a string and its first character."""

def multiple_returns(sentence):
    strtuple = ()
    length = len(sentence)
    first = sentence[0]
    strtuple = length, first
    return strtuple

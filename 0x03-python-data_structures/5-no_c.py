#!/usr/bin/python3

"""
     removes all characters c and C from a string.
     """


def no_c(my_string):
    new_string = my_string.translate({ord(j): None for j in 'Cc'})
    return new_string

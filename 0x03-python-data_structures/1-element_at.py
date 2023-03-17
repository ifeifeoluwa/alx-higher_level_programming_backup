#!/usr/bin/python3

"""
    this function retrieves an element from a list as in C
    """

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return 'None'
    else:
        return my_list[idx]

#!/usr/bin/python3

"""
    function that finds all multiples of 2 in a list.
    """


def divisible_by_2(my_list=[]):
    newlist = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)
    return 

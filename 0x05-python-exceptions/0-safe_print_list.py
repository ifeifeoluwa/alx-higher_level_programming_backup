#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for j in range(x):
        try:
            print(my_list[j], end="")
            c += 1
        except IndexError:
            break
    print()
    return c

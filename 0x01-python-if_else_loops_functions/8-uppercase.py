#!/usr/bin/python3
def ucase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            ab = 32
        else:
            ab = 0
        print("{}".format(ord(str[i]) - ab), end='')
    print()

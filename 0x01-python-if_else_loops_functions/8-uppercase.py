#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            ab = 32
        else:
            ab = 0
        print("{:c}".format(ord(str[i]) - ab), end='')
    print()

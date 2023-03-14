#!/usr/bin/python3
for counter in range(122, 96, -1):
    if counter % 2 == 0:
        print("{}".format(chr(counter)), end="")
    else:
        print("{}".format(chr(counter - 32)), end="")

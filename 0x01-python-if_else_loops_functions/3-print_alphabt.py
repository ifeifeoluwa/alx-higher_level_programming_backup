#!/usr/bin/python3
for ab in range(26):
    if ab != 4 and ab != 16:
        print("{:s}".format(chr(ab + ord("a"))), end="")

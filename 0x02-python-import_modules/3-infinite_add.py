#!/usr/bin/python3

""" program prints the result of the addition of all arguments """

if __name__ == "__main__":

    import sys

    counter = len(sys.argv) - 1
    sumargv = 0

    for n in range(counter):
        sumargv += int(sys.argv[n + 1])
    print(sumargv)

#!/usr/bin/python3
for num in range(0, 100):
    if num != 99:
        print("{}, ".format("0" + str(num) if num < 10 else num), end="")
    else:
        print(num)

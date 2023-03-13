#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

absnum = abs(number)
lastdigit = absnum % 10
if number >= 0:
    if lastdigit > 5:
        print("Last digit of {} is {} and is greater than 5"
                .format(number, lastdigit))
    elif lastdigit == 0:
        print("Last digit of", number, "is", lastdigit,
                "and is 0")
    else:
        print("Last digit of", number, "is", lastdigit,
                "and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", -lastdigit, 
            "and is less than 6 and not 0")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absnum = abs(number)
lastdigit = absnum % 10
gr5msg = "Last digit of {} is {} and is greater than 5"
zeromsg = "Last digit of {} is {} and is 0"
notzeromsg = "Last digit of {} is {} and is less than 6 and not 0"
if number >= 0:
    if lastdigit > 5:
        print(gr5msg.format(number, lastdigit))
    elif lastdigit == 0:
        print(zeromsg.format(number, lastdigit))
    else:
        print(notzeromsg.format(number, lastdigit))
else:
    print(notzeromsg.format(number, -lastdigit))

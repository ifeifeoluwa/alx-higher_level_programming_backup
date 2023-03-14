#!/usr/bin/python3
def fizzbuzz():
    for counter in range(1, 101):
        if counter % 3 == 0 and counter % 5 == 0:
            status = "FizzBuzz"
        elif counter % 3 == 0:
            status = "Fizz"
        elif counter % 5 == 0:
            status = "Buzz"
        else:
            status = counter
        print("{}".format(status), end=" ")

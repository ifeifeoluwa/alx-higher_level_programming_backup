#!/usr/bin/python3
for i in range(100):
    if i / 10 != i % 10 and i / 10 < i % 10:
        print("{}{}".format(int(i / 10), str(i % 10) + ", "
            if i != 89 else i % 10), end="")
print("")

#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    for c in range(len(str)):
        if c != n:
            return (str[:n] + str[n + 1:])

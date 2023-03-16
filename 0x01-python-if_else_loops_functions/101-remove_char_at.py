#!/usr/bin/python3
def remove_char_at(str, n):
    for c in range(len(str)):
        if c != n:
            print("{}".format((str[c])), end="")
    return 




#!/usr/bin/python3
def remove_char_at(str, n):
    for c in range(len(str)):
        if c != n:



            str =+ str[c]
            return (str)
    
    
print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))



def remove_char_at(str, n):
    nstr = ""
    for c in range(len(str)):
        if c != n:
            nstr += str[c]
        return (nstr)

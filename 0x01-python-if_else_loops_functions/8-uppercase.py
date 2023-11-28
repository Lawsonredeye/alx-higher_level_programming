#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            value = ord(i) - 32
            value = chr(value)
            new_str += value
        else:
            value = i
            new_str += i
    print("{}".format(new_str))

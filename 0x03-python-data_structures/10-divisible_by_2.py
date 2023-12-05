#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if not my_list:
        return None
    for i in my_list:
        if i % 2 != 0:
            new_list.append(False)
        elif i % 2 == 0:
            new_list.append(True)
    return (new_list)

#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    total = 0
    new_list = list(set(new_list))
    for i in range(len(new_list)):
        total += new_list[i]
    return total

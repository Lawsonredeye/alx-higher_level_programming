#!/usr/bin/python3
def fizzbuzz():

    for i in range(1, 101):
        # print (f"i = {i}, mod:{i % 3}")
        if i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        if i % (3 * 5) == 0:
            print("FIZZBUZZ", end=' ')
        else:
            print(i, end=' ')

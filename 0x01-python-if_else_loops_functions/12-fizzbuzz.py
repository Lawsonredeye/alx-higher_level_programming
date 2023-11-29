#!/usr/bin/python3
def fizzbuzz():

    for i in range(1, 101):
        # Edge cases to check for the multiples of 3 and 5, 3 or 5            if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')

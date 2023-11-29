#!/usr/bin/python3
def print_last_digit(number):
    value = number % 10
    if number < 0:
        value = number % -10
        value *= -1
    print(value, end="")
    return (value)

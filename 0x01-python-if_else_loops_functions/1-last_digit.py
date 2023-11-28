#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = str(number) #type cast the int
number3 = int(number2[-1]) #stored the sliced string and typecast it
if number3 > 5:
    print(f"Last digit of {number} is {number3} and is greater than 5")
elif number3 == 0:
    print(f"Last digit of {number} is {number3}")
elif number3 < 6 and number3 != 0:
    print(f"Last digit of {number} is {number3} and is less than 6 and not 0")

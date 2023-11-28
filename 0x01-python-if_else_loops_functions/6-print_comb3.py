#!/usr/bin/python3
for i in range(10):
    # Start the inner loop from i + 1
    for j in range(i + 1, 10):
        if j == 9 and i == 8:
            print("{}{}".format(i, j))
            break
        else:
            print("{}{},".format(i, j), end=' ')

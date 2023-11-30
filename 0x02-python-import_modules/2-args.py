#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv) == 1:
        print("1 argument:")
        for i, argument in enumerate(argv, start=1):
            print("{}: {}".format(i, argument))
    else:
        print("{} arguments:".format(len(argv)))
        for i, argument in enumerate(argv, start=1):
            print("{}: {}".format(i, argument))

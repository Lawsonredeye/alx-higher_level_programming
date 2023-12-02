#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    total = 0
    for i in argv:
        total += int(i)
    print(total)

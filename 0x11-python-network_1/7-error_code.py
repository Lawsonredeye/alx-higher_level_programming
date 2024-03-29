#!/usr/bin/python3
"""Script which uses request library instead of urllib"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code == 200:
        print(r.text)
    elif r.status_code >= 400:
        print("Error code: ", r.status_code)

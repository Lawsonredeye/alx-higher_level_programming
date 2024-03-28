#!/usr/bin/python3
"""Script which uses request library instead of urllib"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])

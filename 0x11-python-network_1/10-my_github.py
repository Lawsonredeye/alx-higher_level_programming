#!/usr/bin/python3
"""Script which uses request library instead of urllib"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'

    r = requests.get(url, auth=(username, passwd))
    if r.status_code == 200:
        try:
            obj = r.json()
            print(obj['id'])
        except requests.exceptions.JSONDecodeError:
            print("None")
    else:
        print("None")

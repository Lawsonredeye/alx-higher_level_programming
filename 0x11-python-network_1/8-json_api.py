#!/usr/bin/python3
"""Script which uses request library instead of urllib"""

import requests
import sys

if __name__ == "__main__":
    try:
        q = sys.argv[1]
    except IndexError:
        q = ""
    q = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=q)
    try:
        obj = r.json()
        if not obj:
            print('No result')
        else:
            print(f"[{obj['id']}] {obj['name']}")
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')

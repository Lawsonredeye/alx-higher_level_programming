#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response.
"""
import urllib.request
import urllib.parse
import urllib
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)

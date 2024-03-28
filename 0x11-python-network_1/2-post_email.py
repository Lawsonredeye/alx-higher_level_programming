#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = sys.argv[2]
    data = data.encode()
    req = urllib.request.Request(sys.argv[1], data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        body = response.read().decode()
        print(body)

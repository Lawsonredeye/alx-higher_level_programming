#!/usr/bin/python3
"""
Fetches commits from a github profile thats passed
on the command line using the requests lib and sys module
"""
# get a response from the github profile
# pass the username as the argument as owner
# pass the third argument 



import sys
import requests

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', )
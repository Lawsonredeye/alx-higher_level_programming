#!/usr/bin/python3
"""Script which uses request library instead of urllib"""

import requests


r = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print('\t- type:', type(r.text))
print('\t- content:', r.text)

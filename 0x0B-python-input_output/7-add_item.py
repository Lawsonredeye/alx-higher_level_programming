#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then save them to a file using json and files
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


value = []
start = len(sys.argv)
for i in range(1, start):
    value.append(sys.argv[i])
save_to_json_file(value, "add_item.json")
load_from_json_file("add_item.json")
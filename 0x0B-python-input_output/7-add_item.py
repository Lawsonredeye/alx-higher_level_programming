#!/usr/bin/python3
"""
Script that creates an
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
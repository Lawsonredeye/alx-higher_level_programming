#!/usr/bin/bash
def magic_string():
    magic_string.count += 1
    return "BestSchool" * magic_string.count
magic_string.count = 0

#!/usr/bin/python3
def magic_calculation(a, b):
    return (98 + (a**b))

# Import dis module 
# Use dis.dis to get the byte code of the passed variable
import dis
dis.dis(magic_calculation)

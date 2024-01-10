#!/usr/bin/python3
"""
function that appends to the end of a file without clearing the current data
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added

    Args:
        filename (str): path to the file to be written to
        text (str): string to be appended into the existing file
    """
    with open(filename, "a+", encoding="UTF-8") as f:
        write_data = f.write(text)
        return write_data
nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
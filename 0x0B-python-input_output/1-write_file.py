#!/usr/bin/python3
""" Write to a file module """


def write_file(filename="", text=""):
    """ Writes a string to a text file (UTF8) and
    returns the number of characters written """
    counter = 0
    with open(filename, mode='w', encoding="utf-8") as files:
        files.write(text)
    with open(filename, encoding='utf-8') as a_file:
        counter = a_file.read()
    return len(counter)

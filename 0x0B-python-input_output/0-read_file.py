#!/usr/bin/python3
""" Read file module """


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout """
    with open(filename, encoding="utf-8") as files:
        file_content = files.read()
        for a_lines in file_content:
            print(a_lines, end="")

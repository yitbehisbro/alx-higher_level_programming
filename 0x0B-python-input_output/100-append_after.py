#!/usr/bin/python3
""" Search and update module """


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file, after each line containing
    a specific string
    """
    result = []
    with open(filename, 'r', encoding="utf-8") as a_file:
        for content in a_file:
            result += [content]
            if content.find(search_string) != -1:
                result += [new_string]

    with open(filename, 'w', encoding="utf-8") as a_file:
        a_file.write("".join(result))

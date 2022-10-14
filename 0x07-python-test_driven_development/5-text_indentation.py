#!/usr/bin/python3
""" Text indentation """


def text_indentation(text):
    """ Prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text (str): the text to be displays
    Raises:
        TypeError: incase not string
    """
    if type(text) is str:
        t = text[:]

        for c in ".?:":
            full_text = t.split(c)
            t = ""
            for i in full_text:
                i = i.strip(" ")
                t = i + c if t == "" else t + "\n\n" + i + c
        print(t[:-3], end="")
    else:
        raise TypeError("text must be a string")

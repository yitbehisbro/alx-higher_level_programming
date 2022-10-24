#!/usr/bin/python3
""" My integer module """


class MyInt(int):
    """ MyInt that inherits from int """

    def __ne__(self, integer):
        """ Returns == check for the class """
        return int.__eq__(self, integer)

    def __eq__(self, integer):
        """ Returns != check for the class """
        return int.__ne__(self, integer)

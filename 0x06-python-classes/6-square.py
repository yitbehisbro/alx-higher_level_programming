#!/usr/bin/python3
""" This module does the calculation for area.
"""


class Square:
    """ This class do calculation for square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """ This is the intialization builtin fuction.
        Args:
            size (int): the size of squares
            position (int): the position of blank
        Raises:
            ValueError: raises the value error exception
            TypeError: raises the type error in case -ve number
        """
        self.__size = size
        self.position = position
        if isinstance(self.__size, int):
            if self.__size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Returns the size of the area.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ This is the function that retrieve size.
        Returns: the retrived size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ This is the function that set size.
        Args:
            value (int): the size of squares
        Raises:
            ValueError: raises the value error exception
            TypeError: raises the type error in case -ve number
        """
        self.__size = value
        if isinstance(self.__size, int):
            if self.__size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """ Prints the square with hash tag.
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")

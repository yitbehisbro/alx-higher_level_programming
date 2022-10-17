#!/usr/bin/python3
""" The Rectangle class """


class Rectangle:
    """ Class for rectangle calculation """
    def __init__(self, width=0, height=0):
        """ This is the intialization builtin fuction.
        Args:
            width (int): the width of rectangles
            height (int): the height of rectangles
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ This is the function that retrieve size.
        Returns: the retrived height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ This is the function that set height.
        Args:
            value (int): the height of rectangles
        Raises:
            ValueError: raises the value error exception
            TypeError: raises the type error in case -ve number
        """
        self.__height = value
        if isinstance(self.__height, int):
            if self.__height < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """ This is the function that retrieve width.
        Returns: the retrived width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ This is the function that set size.
        Args:
            value (int): the width of rectangles
        Raises:
            ValueError: raises the value error exception
            TypeError: raises the type error in case -ve number
        """
        self.__width = value
        if isinstance(self.__width, int):
            if self.__width < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

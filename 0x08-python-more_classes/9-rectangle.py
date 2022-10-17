#!/usr/bin/python3
""" The Rectangle class """


class Rectangle:
    """ Class for rectangle calculation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ This is the intialization builtin fuction.
        Args:
            width (int): the width of rectangles
            height (int): the height of rectangles
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ Returns printable string representation of the rectangle
        """
        text = ""
        if self.__width != 0 and self.__height != 0:
            text += "\n".join(str(self.print_symbol) * self.__width
                              for i in range(self.__height))
        return text

    def __repr__(self):
        """ Returns a string representation of the rectangle to be able to
        recreate a new instance by using eval()
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Prints when the del function called
        """
        print("Bye rectangle...", end="\n")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares the two passed rectangle
            Args:
                rect_1 (Rectangle): area of rectangle 1
                rect_2 (Rectangle): area of rectangle 2
            Raises:
                TypeError: if the args are not instance of Rectangle
            Returns:
                The area of rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Class method to print the area when width == height == size
        """
        return cls(size, size)

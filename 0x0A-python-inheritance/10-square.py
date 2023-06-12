#!/usr/bin/python3

""" Module that inherits from 9-rectangle.py """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class that inherits from the previous class """

    def __init__(self, size):
        """
            Initializing the values of Square.

            Args:
                size: the size of the square
        """

        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

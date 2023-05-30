#!/usr/bin/python3
# https://github.com/FabPaul
""" Area of a square """


class Square:
    """ Definition of the class Square """

    def __init__(self, size=0):
        """ Passing of arguments into the square.
        Args:
            size: size of the square'
        Raise:
            TypeError: if size is not an interger.
            ValueError: if type is less than zero.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """ To retrieve the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an interger')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """ Function to calculate the area of the square.
        Return: the square area
        """

        return self.__size ** 2

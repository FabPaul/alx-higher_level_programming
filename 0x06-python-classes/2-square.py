#!/usr/bin/python3
# https://github.com/FabPaul
""" Creating a class Square with specific attributes """


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
            raise TypeError('size must be an interger')

        if size < 0:
            raise ValueError('size must be >=0')

        self.__size = size

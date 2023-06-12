#!/usr/bin/python3

""" Module that inherits from a previous module """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A Rectangle class with logic inherited from another class """

    def __init__(self, width, height):
        """
            Initializing the values of the rectangles.

            Args:
                width: the width of the rectangle
                height: the height of the rectangle
        """

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """ Function to get the area of a rectangle """

        return self.__height * self.__width

    def __str__(self):
        """ String presentation of the Rectangle """

        return f'[{self.__class__.__name__}] {self.__width}/{self.__height}'

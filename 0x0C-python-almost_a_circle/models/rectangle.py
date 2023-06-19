#!/usr/bin/python3

""" Module of a class that defines a Rectangle that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ A rectangle class that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Function that initializes a new instance for the Rectangle """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ To retrieve the width of the rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ to set the width of the rectangle """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        elif value <= 0:
            raise ValueError('width must be > 0')

        else:
            self.__width = value

    @property
    def height(self):
        """ To retrieve the height of the rectangle """

        return self.__height

    @height.setter
    def height(self, value):
        """ To set the height of the rectangle """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        elif value <= 0:
            raise ValueError('height must be > 0')

        else:
            self.__height = value

    @property
    def x(self):
        """ To retrieve the x attribute of the rectangle """

        return self.__x

    @x.setter
    def x(self, value):
        """ to set the x attribute of the rectangle """

        if not isinstance(value, int):
            raise TypeError('x must be an integer')

        elif value < 0:
            raise ValueError('x must be >= 0')

        else:
            self.__x = value

    @property
    def y(self):
        """ To retrieve the y attribute of the rectangle """

        return self.__y

    @y.setter
    def y(self, value):
        """ To set the y attribute of the rectangle """

        if not isinstance(value, int):
            raise TypeError('y must be an integer')

        elif value < 0:
            raise ValueError('y must be >= 0')

        else:
            self.__y = value

    def area(self):
        """ Function that returns the area of the rectangle """

        return self.width * self.height

    def display(self):
        """ Prints in stdout the Rectangle instance with char # """
        
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """ Returns a string representation of the rectangle instance """

        return ('[Rectangle] ({}) {}/{} - {}/{}'
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ Function that assigns arguments to each attribute """

        if len(args) > 0:
            self.id = args[0]

        if len(args) > 1:
            self.width = args[1]

        if len(args) > 2:
            self.height = args[2]

        if len(args) > 3:
            self.x = args[3]

        if len(args) > 4:
            self.y = args[4]

        if len(args) == 0 or len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

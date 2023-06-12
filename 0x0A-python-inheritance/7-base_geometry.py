#!/usr/bin/python3

""" Module for a empty class BaseGeometry """


class BaseGeometry:
    """ A class BaseGeometry """

    def area(self):
        """ FUnction that raises an exception message in a class """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
            Function that validation value

            Args:
                name: the name of the validator
                value: The value of the validator

            Raises:
                TypeError: If value is not an integer
                ValueError: If value is less than or equal to 0
        """

        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

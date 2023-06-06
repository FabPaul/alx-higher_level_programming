#!/usr/bin/python3

""" A module that adds intergers and will take 1 function """


def add_integer(a, b=98):
    """ The function should return the sum of 2 integers or floats as integers.

    Args:
        a: The first parameter.
        b: The second parameter.

    Returns:
        The sum of the parameters.

    Raises:
        TypeError if a or b are neither integers nor floats
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)

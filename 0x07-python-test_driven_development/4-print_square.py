#!/usr/bin/python3

""" Module to print a square """


def print_square(size):
    
    """ 
    Function that prints a square with the character '#'.

    Args:
        Size: Size of the square

    Raises:
        TypeError: If size 'isn't an integer' or 'float and greater than zero'
        ValueError: If size is less than zero
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if not isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for rows in range(0, size):
        for columns in range(size):
            print('#', end='')
        print('')

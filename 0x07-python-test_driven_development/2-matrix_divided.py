#!/usr/bin/python3

""" A module that defines a matrix """


def matrix_divided(matrix, div):
    """
    The function divides all elements of a matrix by a given parameter.

    Args:
        matrix: A list of lists containing integers or floats.
        div: A number to divide the matrix elements (could be integer or float)

    Raises:
        TypeError: If the matrix isn't a list of lists of integers or floats.
        TypeError: If the rows of the matrix are of different sizes.
        TypeError: If the div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Returns:
        A new matrix
    """

    if (
            not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) for row in matrix) or
            not all(
                isinstance(param, (int, float))
                for row in matrix
                for param in row)):
        raise TypeError('matrix must be a matrix (list of lists)'
                        ' of integers/floats')
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        div_row = [round(parameter / div, 2) for parameter in row]
        new_matrix.append(div_row)
    return new_matrix

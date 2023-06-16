#!/usr/bin/python3

""" Module that defines a function representing Pscal's triangle """


def pascal_triangle(n):
    """ Function that returns a list of Pascal's trianggle of size n """

    """ if n is not bigger than 0, return an empty list """

    if n <= 0:
        return []

    """ set up the first row of the triangle """
    triangle = [[1]]

    for ele in range(1, n):
        """ loop through and get the first element of the row """
        prev_row = triangle[ele - 1]
        """ The first element of the current row is uasually one """
        temp = [1]

        for val in range(1, ele):
            """ Loop through the values of the row """
            present_value = prev_row[val - 1] + prev_row[val]
            """ Add the elements from the previous row """
            temp.append(present_value)
            """ Append (add) the calculated value to the current row """

        temp.append(1)
        """ In Pascal's triangle, the last element of the current row is 1 """

        triangle.append(temp)
        """Add the current row to the triangle """

    return triangle

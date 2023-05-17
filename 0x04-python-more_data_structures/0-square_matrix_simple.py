#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    square_int_matrix = [list(map(lambda i: i ** 2, j)) for j in matrix]

    return square_int_matrix

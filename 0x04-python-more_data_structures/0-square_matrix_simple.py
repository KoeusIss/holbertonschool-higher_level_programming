#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of matrix
    """
    return [[j**2 for j in row] for row in matrix]

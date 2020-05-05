#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers

    Args:
        matrix: a double dimension list

    Returns:
        Nothing, just print out the matrix
    """
    for i in matrix:
        print(*i)

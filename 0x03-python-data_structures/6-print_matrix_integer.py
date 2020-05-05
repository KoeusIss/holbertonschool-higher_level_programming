#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers

    Args:
        matrix: a double dimension list

    Returns:
        Nothing, just print out the matrix
    """
    for item in matrix:
        l = len(item)
        for i in range(l):
            print("{}".format(item[i]), end="\n" if i == l - 1 else " ")

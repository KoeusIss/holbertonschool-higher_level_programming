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
        if l == 0:
            print()
        for i in range(l):
            print("{:d}".format(item[i]), end="\n" if i == l - 1 else " ")

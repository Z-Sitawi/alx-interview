#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """
    takes a 2D Matrix then rotates it.
    :param matrix: the 2D matrix
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for idx in range(len(matrix)):
        matrix[idx].reverse()

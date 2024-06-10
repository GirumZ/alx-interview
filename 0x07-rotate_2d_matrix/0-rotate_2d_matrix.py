#!/usr/bin/python3
""" Matrix rotation
"""


def rotate_2d_matrix(matrix):
    """ A function that rotates a matrix"""

    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

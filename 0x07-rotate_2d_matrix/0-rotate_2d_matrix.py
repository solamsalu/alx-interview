#!/usr/bin/python3
""" Task 0: rotating 2d matrix 90 degree clockwise"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Create a copy of the original matrix
    original_matrix = [row[:] for row in matrix]

    # Transpose the matrix
    for i in range(n):
        for j in range(n):
            matrix[i][j] = original_matrix[n - j - 1][i]

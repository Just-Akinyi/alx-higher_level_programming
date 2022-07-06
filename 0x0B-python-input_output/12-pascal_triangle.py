#!/usr/bin/python3
"""Deine class_to_json function"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing
    the Pascal’s triangle of n
    """

    triangle = []

    if n <= 0:
        return triangle
    if n == 1:
        triangle.append([1])
        return triangle
    if n == 2:
        triangle.extend([[1], [1, 1]])
        return triangle

    if n > 2:
        triangle.extend([[1], [1, 1]])
        for n_row in range(3, n+1):
            row = [1]
            for i in range(n_row-3):
                row.append(sum(triangle[-1][0 + i:2 + i]))
            row.extend([n_row-1, 1])
            triangle.append(row)

    return triangle

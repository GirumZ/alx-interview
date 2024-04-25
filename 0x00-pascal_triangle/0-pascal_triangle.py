#!/usr/bin/python3

"""
Python function that takes an intiger n and
returns a pascal trinagle of size  n
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    trinagle = [[1]]

    for i in range(1, n):
        prev_row = trinagle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        trinagle.append(new_row)

    return trinagle

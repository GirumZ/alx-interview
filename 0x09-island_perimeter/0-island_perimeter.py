#!/usr/bin/python3
""" Island preimeter"""


def island_perimeter(grid):
    """ Function to calculate the perimeter of an island"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if grid[i - 1][j] != 1:
                    perimeter += 1
                if grid[i + 1][j] != 1:
                    perimeter += 1
                if grid[i][j - 1] != 1:
                    perimeter += 1
                if grid[i][j + 1] != 1:
                    perimeter += 1
    return perimeter

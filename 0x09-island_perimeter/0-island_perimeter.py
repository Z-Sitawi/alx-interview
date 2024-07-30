#!/usr/bin/python3
"""
    Calculating the Island Perimeter
"""


def island_perimeter(grid):
    """
        Calculates the perimeter of an island based on the given grid

    :param grid: Is a list of lists of integers:
                0 represents water
                1 represents land
                Each cell is square, with a side length of 1
                Cells are connected horizontally/vertically (not diagonally).
                grid is rectangular & its width and height not exceeding 100

    :return: The perimeter of the island described in grid
    """
    if not grid:
        return 0

    width = 0
    height = 0
    for row in grid:
        if 1 in row:
            height += 1
        count = 0
        for x in row:
            if x == 1:
                count += 1
        if count > width:
            width = count

    if (height > 100 or width > 100) or (height == 0 or width == 0):
        return 0
    else:
        return (height + width) * 2

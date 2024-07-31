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
    perimeter = 0
    if len(grid) == 0:
        return perimeter

    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            if grid[row][cell] == 1:

                """ Check up"""
                row_idx = row - 1
                if row_idx < 0 or grid[row_idx][cell] == 0:
                    perimeter += 1

                """ Check down"""
                row_idx = row + 1
                if row_idx >= len(grid) or grid[row_idx][cell] == 0:
                    perimeter += 1

                """ Check left"""
                cell_idx = cell - 1
                if cell_idx < 0 or grid[row][cell_idx] == 0:
                    perimeter += 1

                """ Check right"""
                cell_idx = cell + 1
                if cell_idx >= len(grid[row]) or grid[row][cell_idx] == 0:
                    perimeter += 1
    return perimeter


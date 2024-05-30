#!/usr/bin/python3
def pascal_triangle(n):
    """
    Args:
        n: number of rows in the triangle

    Returns: A list of lists of integers representing the Pascal’s triangle

    """
    if n <= 0:
        return []

    triangle = []
    for row in range(n):
        row_data = []
        for col in range(row + 1):
            if col == 0 or col == row:
                row_data.append(1)
            else:
                prev_row = triangle[row - 1]
                col_data = prev_row[col - 1] + prev_row[col]
                row_data.append(col_data)
        triangle.append(row_data)
    return triangle

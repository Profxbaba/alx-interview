#!/usr/bin/python3
"""
Module to calculate the perimeter of an island described in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list of list of int): The grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for the current land cell
                perimeter += 4

                # Subtract 1 for each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:  # Check cell above
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Check cell below
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Check cell to the left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Check cell right
                    perimeter -= 1

    return perimeter

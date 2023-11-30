#!/usr/bin/python3
"""Module for Island Perimeter
"""


def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    no_island = 0
    perimeter = 0

    def dfs(i, j):
        nonlocal perimeter
        nonlocal no_island

        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
            perimeter += 1
            return

        if grid[i][j] == -1:
            return

        grid[i][j] = -1

        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                no_island += 1
                dfs(i, j)

    if no_island != 1:
        return 0

    return perimeter

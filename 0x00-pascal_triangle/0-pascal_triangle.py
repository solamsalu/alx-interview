#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]
    for row in range(1, n):
        triangle_row = [1]
        for i in range(1, row):
            triangle_row.append(triangle[row - 1][i - 1] + triangle[row - 1][i])
        triangle_row.append(1)
        triangle.append(triangle_row)
    return triangle

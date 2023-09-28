def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    for row in range(n):
        triangle_row = [1] * (row + 1)
        if row > 1:
            for i in range(1, row):
                triangle_row[i] = triangle[row - 1][i - 1] + triangle[row - 1][i]
        triangle.append(triangle_row)
    return triangle

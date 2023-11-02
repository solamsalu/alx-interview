#!/usr/bin/python3
"""N queens solution finder module.

Usage: nqueens N:
    If the user called the program with the wrong number of arguments, print
        Usage: nqueens N, followed by a new line, and exit with the status 1.
where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number, followed by a new line,
    and exit with the status 1.
    If N is smaller than 4, print N must be at least 4, followed by a new
    line, and exit with the status 1.
The program should print every possible solution to the problem.
    One solution per line.
    Format: see README.
    You don’t have to print the solutions in a specific order.
You are only allowed to import the sys module.
"""
from sys import argv


def is_NQueen(cell: list) -> bool:
    """ False if not N Queen, True if N Queen """
    row_number = len(cell) - 1
    difference = 0
    for index in range(0, row_number):
        difference = cell[index] - cell[row_number]
        if difference < 0:
            difference *= -1
        if difference == 0 or difference == row_number - index:
            return False
    return True


def solve_NQueens(dimension: int, row: int, cell: list, output: list):
    """ Return result of N Queens recursively """
    if row == dimension:
        print(output)
    else:
        for column in range(0, dimension):
            cell.append(column)
            output.append([row, column])
            if (is_NQueen(cell)):
                solve_NQueens(dimension, row + 1, cell, output)
            cell.pop()
            output.pop()


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
try:
    N = int(argv[1])
except BaseException:
    print('N must be a number')
    exit(1)
if N < 4:
    print('N must be at least 4')
    exit(1)
else:
    output = []
    cell = 0
    solve_NQueens(int(N), cell, [], output)

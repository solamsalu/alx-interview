#!/usr/bin/python3
""" N queens solution finder module. """
import sys


def print_board(board):
    """Prints the board"""
    print([[col for col in row] for row in board])


def is_safe(board, row, col):
    """Checks if a position is safe"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col):
    """Solves the N queens problem"""
    if col >= len(board):
        print_board(board)
        print("\n")
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1) or res
            board[i][col] = 0
    return res


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0]*N for _ in range(N)]
    if not solve_nqueens(board, 0):
        print("Solution does not exist")
        return
    sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/python3
""" N Queens"""
import sys


def checker(board, row, col):
    """ checks if the cell is available"""

    for i in range(row):
        if board[i] == col or board[i] - i == col - row \
                or board[i] + i == col + row:
            return False
    return True


def solve_board(N):
    """ Solves the board for the queen positions"""

    def solve(row, board):
        """ Solves the board for the queen positions"""

        if row == N:
            print([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if checker(board, row, col):
                board[row] = col
                solve(row + 1, board)
                board[row] = -1

    board = [-1] * N
    solve(0, board)


def main():
    """ Main entry point"""

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

    solve_board(N)


if __name__ == "__main__":
    main()

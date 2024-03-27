from math import floor
from random import choice

from numpy import full
from .sudoku_solver import SudokuSolver


class SudokuCreator:
    def seed_board(self, size: int):
        board: list[list[int]] = full((size, size), 0).tolist()
        possible_coordinates = range(size)
        board[choice(possible_coordinates)][choice(possible_coordinates)] = (
            choice(possible_coordinates) + 1
        )
        return board

    def empty_board(self, board: list[list[int]], n_empty: int):
        size = len(board)
        empties_per_row = floor(n_empty / size)
        rest_per_row = n_empty % size
        for row in range(size):
            n_to_empty = empties_per_row
            if rest_per_row > 0:
                n_to_empty += 1
                rest_per_row -= 1
            for _ in range(n_to_empty):
                coordinates_to_try: list[int] = [n for n in range(size)]
                while len(coordinates_to_try) > 0:
                    random_column = choice(coordinates_to_try)
                    coordinates_to_try.remove(random_column)
                    if board[row][random_column] != 0:
                        board[row][random_column] = 0
                        break

    def create_board(self, n: int, n_empty: int):
        size = n * n
        board = self.seed_board(size)
        board = SudokuSolver().solve(board)
        self.empty_board(board, n_empty)
        # print(array(board))
        return board

import copy
from math import floor, sqrt


class SudokuSolver:
    def column_to_array(self, board: list[list[int]], column: int):
        array: list[int] = []
        for row in range(len(board)):
            array.append(board[row][column])
        return array

    def zone_to_array(
        self, board: list[list[int]], row: int, column: int, zone_size: int
    ):
        array: list[int] = []
        for x in range(row, row + zone_size):
            for y in range(column, column + zone_size):
                array.append(board[x][y])
        return array

    def can_solve(
        self, board: list[list[int]], row: int, column: int, number: int
    ):
        if number in board[row]:
            # print(f"FOR {row},{column} and {number} CANNOT row")
            return False
        if number in self.column_to_array(board, column):
            # print(f"FOR {row},{column} and {number} CANNOT column")
            return False
        zone_size = floor(sqrt(len(board)))
        zone_row = floor(row / zone_size) * zone_size
        zone_column = floor(column / zone_size) * zone_size
        if number in self.zone_to_array(
            board, zone_row, zone_column, zone_size
        ):
            # print(f"FOR {row},{column} and {number} CANNOT zone")
            return False
        return True

    def find_empties(self, board: list[list[int]]):
        empties: list[tuple[int, int]] = []
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == 0:
                    empties.append((row, column))
        return empties

    def solve_board(
        self, board: list[list[int]], empties: list[tuple[int, int]]
    ):
        # print(empties)
        # print(nparr(board))
        if len(empties) == 0:
            return board
        row, column = empties.pop(0)
        for number in range(1, len(board) + 1):
            # print(f"FOR {row},{column} TRY {number}")
            if self.can_solve(board, row, column, number):
                next_board = copy.deepcopy(board)
                next_board[row][column] = number
                solution = self.solve_board(next_board, copy.deepcopy(empties))
                if solution is not None:
                    return solution
        return None

    def solve(self, board: list[list[int]]):
        return self.solve_board(copy.deepcopy(board), self.find_empties(board))

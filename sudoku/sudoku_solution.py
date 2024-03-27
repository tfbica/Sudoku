from math import floor, sqrt


class SudokuSolution:
    def is_file_solution(self, file: str):
        pass

    def is_set_valid(self, the_set: set[int], size: int):
        for number in range(1, size + 1):
            if number not in the_set:
                return False
        return True

    def are_rows_valid(self, board: list[int], size: int):
        for row in board:
            if not self.is_set_valid({number for number in row}, size):
                return False
        return True

    def are_columns_valid(self, board: list[list[int]], size: int):
        for column in range(0, size):
            column_as_set = {board[row][column] for row in range(0, size)}
            if not self.is_set_valid(column_as_set, size):
                return False
        return True

    def are_zones_valid(self, board: list[list[int]], size: int):
        zones_in_axis = floor(sqrt(size))
        for row in range(0, size, zones_in_axis):
            for column in range(0, size, zones_in_axis):
                zone_as_set: set[int] = set()
                for x in range(row, row + zones_in_axis):
                    for y in range(column, column + zones_in_axis):
                        zone_as_set.add(board[x][y])
                if not self.is_set_valid(zone_as_set, size):
                    return False
        return True

    def is_solution(self, board: list[list[int]]):
        size = len(board)
        if not self.are_rows_valid(board, size):
            return False
        if not self.are_columns_valid(board, size):
            return False
        if not self.are_zones_valid(board, size):
            return False
        return True
    
    def boards_intersect(self, initial_board: list[list[int]], final_board: list[list[int]]):
        for row in range(0, len(initial_board)):
            for col in range(0, len(initial_board[0])):
                if initial_board[row][col] != 0 and initial_board[row][col] != final_board[row][col]:
                    return False
        return True
    
    def is_solution_for(self, initial_board: list[list[int]], final_board: list[list[int]]):
        if len(initial_board) != len(final_board):
            return False
        if not self.boards_intersect(initial_board, final_board):
            return False
        if not self.is_solution(final_board):
            return False
        return True

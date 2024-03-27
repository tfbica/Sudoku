import unittest
from sudoku_solver import SudokuSolver
from sudoku_solution import SudokuSolution


class SudokuSolverShould(unittest.TestCase):
    def test_solves_4(self):
        sudoku = SudokuSolver()
        board = [[1, 0, 3, 0], [3, 0, 0, 2], [0, 3, 0, 1], [0, 1, 0, 3]]
        solution = sudoku.solve(board)
        self.assertIsNotNone(solution)
        self.assertTrue(SudokuSolution().is_solution_for(board, solution))

    def test_solves_9(self):
        sudoku = SudokuSolver()
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 5, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 4, 0, 0, 8, 0, 0, 7, 9],
        ]
        solution = sudoku.solve(board)
        self.assertIsNotNone(solution)
        self.assertTrue(SudokuSolution().is_solution_for(board, solution))

    def test_unsolvable_4(self):
        sudoku = SudokuSolver()
        board = [
            [1, 0, 3, 4],
            [3, 4, 1, 2],
            [0, 3, 2, 1],
            [4, 1, 0, 3],
        ]
        self.assertIsNone(sudoku.solve(board))

    def test_unsolvable_9(self):
        sudoku = SudokuSolver()
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [6, 0, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
        self.assertIsNone(sudoku.solve(board))


if __name__ == "__main__":
    unittest.main()

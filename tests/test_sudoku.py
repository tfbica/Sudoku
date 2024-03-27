import os
import sys
import unittest

# Add the parent directory of your module to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from sudoku import SudokuSolution


class SudokuSolutionShould(unittest.TestCase):
    def test_is_solution_4(self):
        sudoku = SudokuSolution()
        self.assertTrue(
            sudoku.is_solution([[1, 2, 3, 4], [3, 4, 1, 2], [2, 3, 4, 1], [4, 1, 2, 3]])
        )

    def test_is_not_solution_because_wrong_row(self):
        sudoku = SudokuSolution()
        self.assertFalse(
            sudoku.is_solution([[1, 2, 3, 4], [3, 4, 1, 2], [2, 3, 4, 1], [4, 1, 2, 1]])
        )

    def test_is_not_solution_because_wrong_column(self):
        sudoku = SudokuSolution()
        self.assertFalse(
            sudoku.is_solution([[1, 2, 3, 4], [3, 4, 1, 2], [3, 4, 1, 2], [4, 1, 2, 3]])
        )

    def test_is_not_solution_because_zone(self):
        sudoku = SudokuSolution()
        self.assertFalse(
            sudoku.is_solution([[1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 1, 2], [4, 3, 2, 1]])
        )

    def test_is_solution_9(self):
        sudoku = SudokuSolution()
        self.assertTrue(
            sudoku.is_solution(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9],
                ]
            )
        )

    def test_is_solution_for(self):
        sudoku = SudokuSolution()
        self.assertTrue(
            sudoku.is_solution_for(
                [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 5, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 4, 0, 0, 8, 0, 0, 7, 9],
                ],
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9],
                ],
            )
        )

    def test_is_not_solution_for_because_not_solution(self):
        sudoku = SudokuSolution()
        self.assertFalse(
            sudoku.is_solution_for(
                [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 5, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 4, 0, 0, 8, 0, 0, 7, 9],
                ],
                [
                    [5, 3, 4, 5, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9],
                ],
            )
        )

    def test_is_not_solution_for_because_different(self):
        sudoku = SudokuSolution()
        self.assertFalse(
            sudoku.is_solution_for(
                [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 5, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 4, 0, 0, 8, 0, 0, 7, 9],
                ],
                [
                    [4, 5, 3, 8, 2, 6, 1, 9, 7],
                    [8, 9, 2, 5, 7, 1, 6, 3, 4],
                    [1, 6, 7, 4, 9, 3, 5, 2, 8],
                    [7, 1, 4, 9, 5, 2, 8, 6, 3],
                    [5, 8, 6, 1, 3, 7, 2, 4, 9],
                    [3, 2, 9, 6, 8, 4, 7, 5, 1],
                    [9, 3, 5, 2, 1, 8, 4, 7, 6],
                    [6, 7, 1, 3, 4, 5, 9, 8, 2],
                    [2, 4, 8, 7, 6, 9, 3, 1, 5],
                ],
            )
        )


if __name__ == "__main__":
    unittest.main()

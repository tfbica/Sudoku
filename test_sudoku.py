import unittest


from sudoku_solution import SudokuSolution


class SudokuSolutionShould(unittest.TestCase):
    def test_is_solution(self):
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

    def test_is_solution_for_9(self):
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


if __name__ == "__main__":
    unittest.main()

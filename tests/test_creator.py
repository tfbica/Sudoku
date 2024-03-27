import os
import sys
import unittest

# Add the parent directory of your module to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from sudoku import SudokuCreator


class SudokuCreatorShould(unittest.TestCase):
    def count_empties(self, board, size):
        n_empty = 0
        for row in range(size):
            for column in range(size):
                if board[row][column] == 0:
                    n_empty += 1
        return n_empty

    def test_generate_4(self):
        sudoku = SudokuCreator()
        board = sudoku.create_board(2, 8)
        self.assertIsNotNone(board)
        self.assertEqual(8, self.count_empties(board, 2 * 2))

    def test_generate_9(self):
        sudoku = SudokuCreator()
        board = sudoku.create_board(3, 51)
        self.assertIsNotNone(board)
        self.assertEqual(51, self.count_empties(board, 3 * 3))


if __name__ == "__main__":
    unittest.main()

# Sudoku game library

[![Python Tests](https://github.com/tfbica/Sudoku/actions/workflows/python_tests.yml/badge.svg)](https://github.com/tfbica/Sudoku/actions/workflows/python_tests.yml)

The library provides 3 classes.

## SudokuSolution

Checks if a Sudoku board is corretly filled.

```
solution = SudokuSolution()
solution.is_solution(board)
```

or

```
solution = SudokuSolution()
solution.is_solution_for(board, original_board)
```

## SudokuSolver

Solves a Sudoku board.

```
solver = SudokuSolver()
solved_board = solver.solve(board)
```

## SudokuCreator

Creates a Sudoku board, given the root of the size and the number of empty places.

```
creator = SudokuCreator()
board = creator.create_board(3, 51)
```

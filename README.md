# Sudoku game library

## sudoku_solution

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

## sudoku_solver

Solves a Sudoku board.

```
solver = SudokuSolver()
solved_board = solver.solve(board)
```

## sudoku_creator

Creates a Sudoku board, given the root of the size and the number of empty places.

```
creator = SudokuCreator()
board = creator.create_board(3, 51)
```

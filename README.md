# Sudoku

Simple but efficient backtracking solver for Sudoku puzzle.

## Execution
Just input the given Sudoku initial condition as shown in example:
```[bash]
sudoku_giv[0][:] = [9, 0, 6, 0, 7, 0, 4, 0, 3]
sudoku_giv[1][:] = [0, 0, 0, 4, 0, 0, 2, 0, 0]
sudoku_giv[2][:] = [0, 7, 0, 0, 2, 3, 0, 1, 0]
sudoku_giv[3][:] = [5, 0, 0, 0, 0, 0, 1, 0, 0]
sudoku_giv[4][:] = [0, 4, 0, 2, 0, 8, 0, 6, 0]
sudoku_giv[5][:] = [0, 0, 3, 0, 0, 0, 0, 0, 5]
sudoku_giv[6][:] = [0, 3, 0, 7, 0, 0, 0, 5, 0]
sudoku_giv[7][:] = [0, 0, 7, 0, 0, 5, 0, 0, 0]
sudoku_giv[8][:] = [4, 0, 5, 0, 1, 0, 7, 0, 8]
```

Hit run and check the solution\solutions:
```[bash]
Running time: 0.07700 seconds
Total number of corrected solutions: 2
Solution number 1:
[[9 2 6 5 7 1 4 8 3]
 [3 5 1 4 8 6 2 7 9]
 [8 7 4 9 2 3 5 1 6]
 [5 8 2 3 6 7 1 9 4]
 [1 4 9 2 5 8 3 6 7]
 [7 6 3 1 4 9 8 2 5]
 [2 3 8 7 9 4 6 5 1]
 [6 1 7 8 3 5 9 4 2]
 [4 9 5 6 1 2 7 3 8]]
Solution number 2:
[[9 2 6 5 7 1 4 8 3]
 [3 5 1 4 8 6 2 7 9]
 [8 7 4 9 2 3 5 1 6]
 [5 8 2 3 6 7 1 9 4]
 [1 4 9 2 5 8 3 6 7]
 [7 6 3 1 9 4 8 2 5]
 [2 3 8 7 4 9 6 5 1]
 [6 1 7 8 3 5 9 4 2]
 [4 9 5 6 1 2 7 3 8]]
```

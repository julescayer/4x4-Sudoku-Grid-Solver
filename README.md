# 4x4 Sudoku Grid Solver
## Project Description
This project has three main components:
- **Sudoku Puzzle Generator**: Creates random 4x4 sudoku puzzles
- **Backtracking Puzzle Solver**: Implements backtracking algorithm to solve any 4x4 sudoku grid
- **Main File**: Uses the algorithms developed in the previous files to create and then solve a 4x4 sudoku puzzle

## Features
- Generates valid 4x4 Sudoku puzzles with random holes
- Solves puzzles using a backtracking algorithm
- Includes functionality to validate Sudoku rules

## Directions
To run the code, simply run the main.py file which will print the empty puzzle and the agent's solved puzzle. If no solution exists, the code will return "No solution found for the puzzle."

### Example:
Generated Puzzle:
```
. . 4 2
. 4 . 3
. 1 2 4
4 2 . .
```
Solved Puzzle:
```
1 3 4 2
2 4 1 3
3 1 2 4
4 2 3 1
```

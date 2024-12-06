from puzzle_creator import create_sudoku_puzzle, print_board
from backtracking_solver import solve_sudoku

if __name__ == "__main__":
    # Step 1: Generate a Sudoku puzzle
    puzzle = create_sudoku_puzzle()
    print("Generated Sudoku Puzzle:")
    print_board(puzzle)

    # Step 2: Solve the puzzle using backtracking
    print("\nSolving the puzzle...")
    if solve_sudoku(puzzle):
        print("\nSolved Sudoku:")
        print_board(puzzle)
    else:
        print("\nNo solution exists for the given puzzle.")

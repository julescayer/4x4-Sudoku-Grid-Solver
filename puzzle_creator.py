import random

def is_valid(board, row, col, num):
    """Check if a number can be placed in a given cell."""
    for i in range(4):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 2 * (row // 2), 2 * (col // 2)
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if board[i][j] == num:
                return False
    return True

def generate_full_sudoku(board):
    """Generate a complete 4x4 Sudoku board using backtracking."""
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                random_numbers = list(range(1, 5))  # Numbers 1-4
                random.shuffle(random_numbers)    # Shuffle for randomness
                for num in random_numbers:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if generate_full_sudoku(board):
                            return True
                        board[row][col] = 0  # Undo placement (backtrack)
                return False  # If no valid number is found, backtrack
    return True  # If all cells are filled, the board is complete

def remove_numbers(board, num_holes):
    """Remove numbers from a full board to create a solvable puzzle."""
    cells_removed = 0
    while cells_removed < num_holes:
        row, col = random.randint(0, 3), random.randint(0, 3)
        if board[row][col] != 0:  # Only remove filled cells
            board[row][col] = 0
            cells_removed += 1

def create_sudoku_puzzle():
    """Generate a 4x4 Sudoku puzzle."""
    board = [[0 for _ in range(4)] for _ in range(4)]
    if not generate_full_sudoku(board):
        raise ValueError("Failed to generate a valid Sudoku board.")
    num_holes = random.randint(6, 8)  # Randomly remove between 6-8 cells
    remove_numbers(board, num_holes)
    return board

def print_board(board):
    """Print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

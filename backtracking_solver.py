def is_valid(board, row, col, num):
    """Check if a number can be placed in a given cell."""
    # Check row and column
    for i in range(4):
        if board[row][i] == num or board[i][col] == num:
            return False
    # Check 2x2 grid
    start_row, start_col = 2 * (row // 2), 2 * (col // 2)
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if board[i][j] == num:
                return False
    return True


def solve_sudoku(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                for num in range(1, 5):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Import the puzzle generator and RL solver components
import numpy as np
import random

# Puzzle generator functions from earlier
def is_valid(board, row, col, num):
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
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                random_numbers = list(range(1, 5))
                random.shuffle(random_numbers)
                for num in random_numbers:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if generate_full_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def remove_numbers(board, num_holes):
    while num_holes > 0:
        row, col = random.randint(0, 3), random.randint(0, 3)
        if board[row][col] != 0:
            board[row][col] = 0
            num_holes -= 1

def create_sudoku_puzzle():
    board = [[0 for _ in range(4)] for _ in range(4)]
    generate_full_sudoku(board)
    remove_numbers(board, random.randint(6, 8))
    return board

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

# RL environment and agent (from earlier)
class SudokuEnv:
    def __init__(self, puzzle):
        self.grid = np.array(puzzle)
        self.original = np.array(puzzle)
        self.reset()
    
    def reset(self):
        self.state = self.grid.copy()
        return self.state
    
    def is_valid_move(self, row, col, num):
        if num in self.state[row, :] or num in self.state[:, col]:
            return False
        start_row, start_col = 2 * (row // 2), 2 * (col // 2)
        if num in self.state[start_row:start_row+2, start_col:start_col+2]:
            return False
        return True
    
    def step(self, action):
        row, col, num = action
        if self.original[row, col] != 0 or not self.is_valid_move(row, col, num):
            return self.state, -1, False
        self.state[row, col] = num
        if np.all(self.state > 0):  # Check if solved
            return self.state, 100, True
        return self.state, 1, False
    
    def available_actions(self):
        actions = []
        for row in range(4):
            for col in range(4):
                if self.state[row][col] == 0:
                    for num in range(1, 5):
                        actions.append((row, col, num))
        return actions

class QLearningAgent:
    def __init__(self, env, alpha=0.1, gamma=0.99, epsilon=0.1):
        self.env = env
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
    
    def get_q_value(self, state, action):
        return self.q_table.get((tuple(state.flatten()), action), 0)
    
    def update_q_value(self, state, action, reward, next_state):
        old_value = self.get_q_value(state, action)
        next_max = max([self.get_q_value(next_state, a) for a in self.env.available_actions()], default=0)
        self.q_table[(tuple(state.flatten()), action)] = old_value + self.alpha * (reward + self.gamma * next_max - old_value)
    
    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.env.available_actions())
        q_values = [(self.get_q_value(state, action), action) for action in self.env.available_actions()]
        return max(q_values, key=lambda x: x[0])[1]

# Main program
if __name__ == "__main__":
    # Step 1: Create a 4x4 Sudoku puzzle
    puzzle = create_sudoku_puzzle()
    print("Generated Sudoku Puzzle:")
    print_board(puzzle)

    # Step 2: Set up the environment and agent
    env = SudokuEnv(puzzle)
    agent = QLearningAgent(env)

    # Step 3: Train the agent
    print("\nTraining the agent...")
    for episode in range(1000):
        state = env.reset()
        done = False
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.update_q_value(state, action, reward, next_state)
            state = next_state

    # Step 4: Solve the puzzle
    print("\nSolving the puzzle with the trained agent:")
    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(state)
        state, reward, done = env.step(action)
        print_board(state)
        print()

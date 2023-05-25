import random

def generate_random_board(n):
    """Generates a random NxN chess board with N queens"""
    board = [random.randint(0, n-1) for i in range(n)]
    return board

def calculate_attacks(board):
    """Calculates the total number of attacks on the board"""
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                attacks += 1
    return attacks

def move_queen(board):
    """Moves a queen to a better position if possible"""
    n = len(board)
    current_attacks = calculate_attacks(board)
    for i in range(n):
        for j in range(n):
            if j != board[i]:
                new_board = list(board)
                new_board[i] = j
                new_attacks = calculate_attacks(new_board)
                if new_attacks < current_attacks:
                    return new_board
    return board

def hill_climbing(n):
    """Solves the N-Queens problem using hill climbing"""
    board = generate_random_board(n)
    while True:
        current_attacks = calculate_attacks(board)
        if current_attacks == 0:
            return board
        new_board = move_queen(board)
        new_attacks = calculate_attacks(new_board)
        if new_attacks >= current_attacks:
            return board
        board = new_board


def print_board(board):
    """Prints the board in a matrix format"""
    n = len(board)
    for i in range(n):
        row = ["Q" if j == board[i] else "-" for j in range(n)]
        print(" ".join(row))

solution = hill_climbing(8)
print(solution)
print_board(solution)


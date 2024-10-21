# Minimax Algorithm Implementation for Tic-Tac-Toe

# Define the players
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Function to check if there's a winner or if the game is over
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != EMPTY:
            return board[combo[0]]  # Return the winner ('X' or 'O')
    
    if EMPTY not in board:
        return "DRAW"  # It's a draw
    
    return None  # The game is still ongoing

# Minimax function to evaluate the board and make decisions
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    
    # Base cases
    if winner == PLAYER_X:
        return 10 - depth
    elif winner == PLAYER_O:
        return depth - 10
    elif winner == "DRAW":
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                score = minimax(board, depth + 1, True)
                board[i] = EMPTY
                best_score = min(best_score, score)
        return best_score

# Function to find the best move for the current player
def find_best_move(board, player):
    best_move = None
    best_score = -float('inf') if player == PLAYER_X else float('inf')
    
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = player
            score = minimax(board, 0, player == PLAYER_O)
            board[i] = EMPTY
            
            if player == PLAYER_X:
                if score > best_score:
                    best_score = score
                    best_move = i
            else:
                if score < best_score:
                    best_score = score
                    best_move = i
    
    return best_move

# Function to print the board
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])

# Example usage
if __name__ == "__main__":
    # Initial empty board (9 spaces for Tic-Tac-Toe)
    board = [EMPTY] * 9

    # Simulate a game where Player X (AI) plays against Player O
    board[0] = PLAYER_X
    board[1] = PLAYER_O
    board[4] = PLAYER_X
    board[7] = PLAYER_O
    
    print("Current Board:")
    print_board(board)
    
    # Find the best move for Player X
    best_move = find_best_move(board, PLAYER_X)
    
    if best_move is not None:
        print(f"\nBest move for Player X is at position: {best_move}")
    else:
        print("\nNo more moves available.")

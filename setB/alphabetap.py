PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]  
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != EMPTY:
            return board[combo[0]]  # Return the winner ('X' or 'O')
    
    if EMPTY not in board:
        return "DRAW"  # It's a draw
    
    return None  # The game is still ongoing

def alpha_beta(board, depth, alpha, beta, is_maximizing):
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
                score = alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = EMPTY
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:  # Beta cut-off
                    break
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                score = alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = EMPTY
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:  # Alpha cut-off
                    break
        return best_score

def find_best_move_alpha_beta(board, player):
    best_move = None
    best_score = -float('inf') if player == PLAYER_X else float('inf')
    
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = player
            score = alpha_beta(board, 0, -float('inf'), float('inf'), player == PLAYER_O)
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
    
    # Find the best move for Player X using Alpha-Beta Pruning
    best_move = find_best_move_alpha_beta(board, PLAYER_X)
    
    if best_move is not None:
        print(f"\nBest move for Player X is at position: {best_move}")
    else:
        print("\nNo more moves available.")
        
        
        
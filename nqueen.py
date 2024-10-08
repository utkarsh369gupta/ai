def nqueen(n):
    board = [[False for _ in range(n)] for _ in range(n)]
    if not solve_nqueen(board, 0, n):
        print("solution does not exist")
        return False
    display(board, n)
    return True


def solve_nqueen(board, row, n) -> bool:
    if row >= n:
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            
            if solve_nqueen(board, row+1, n):
                return True
        board[row][col] = False
    return False


def is_safe(board, row, col, n) -> bool:
    for i in range(col):
        if (board[row][i] == True):
            return False

    for i in range(row):
        if (board[i][col] == True):
            return False

    min_left = min(row, col)
    for i in range(1, min_left+1):
        if (board[row-i][col-i] == True):
            return False

    min_right = min(row, n-col-1)
    for i in range(1, min_right+1):
        if (board[row-i][col+i] == True):
            return False

    return True


def display(board, n):
    for i in range(n):
        for j in range(n):
            if (board[i][j] == True):
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
        
nqueen(8)

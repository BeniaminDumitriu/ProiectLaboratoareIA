def is_valid(board, row, col, n):
    for i in range(n):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, col, n):
    if col == n:
        return True
    for i in range(n):
        if is_valid(board, i, col, n):
            board[i][col] = 1
            if solve(board, col+1, n):
                return True
            board[i][col] = 0
    return False
def n_queens_backtracking(n):
    board = [[0 for x in range(n)] for y in range(n)]
    if not solve(board, 0, n):
        print("Nu există soluție pentru o tablă de %d x %d." % (n, n))
        return
    print("Soluția pentru o tablă de %d x %d:" % (n, n))
    for row in board:
        print(row)


n_queens_backtracking(4)

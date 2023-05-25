from queue import Queue

def is_valid_move(x, y, board):
    for i in range(x):
        if board[i] == y or abs(i - x) == abs(board[i] - y):
            return False
    return True

def lee_algorithm(n, board):
    """
    Aplică algoritmul lui Lee pentru a găsi cel mai scurt drum care acoperă
    toate celelalte coloane fără să atace reginele deja plasate.
    """
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    q = Queue()
    for i in range(n):
        q.put((i, board[i]))
        dist[i][board[i]] = 0
    while not q.empty():
        x, y = q.get()
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.put((nx, ny))
    return max(max(row) for row in dist)

def queens_lee(n):
    """
    Găsește numărul minim de mutări necesare pentru a plasa cele N regine
    pe o tablă de șah de dimensiune N x N fără să se atace între ele, folosind
    algoritmul lui Lee.
    """
    min_moves = float('inf')
    for i in range(n):
        board = [0] * n
        board[0] = i
        for j in range(1, n):
            for k in range(n):
                if is_valid_move(j, k, board):
                    board[j] = k
                    break
            else:
                j -= 1
                continue
        moves = lee_algorithm(n, board)
        if moves < min_moves:
            min_moves = moves
    return min_moves


n = 8 
min_moves = queens_lee(n)
print(f"Numărul minim de mutări necesare pentru a plasa cele {n} regine este {min_moves}.")

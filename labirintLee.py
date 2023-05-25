from collections import deque

def print_path(parent, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    for cell in path:
        print(cell, end=" ")
    print()

def lee_algorithm(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]

    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    while queue:
        cell = queue.popleft()

        if cell == end:
            print("Calea găsită:")
            print_path(parent, end)
            return

        neighbors = [
            (cell[0] - 1, cell[1]),  # sus
            (cell[0] + 1, cell[1]),  # jos
            (cell[0], cell[1] - 1),  # stânga
            (cell[0], cell[1] + 1)   # dreapta
        ]

        for neighbor in neighbors:
            row, col = neighbor

            if 0 <= row < rows and 0 <= col < cols and maze[row][col] != 1 and not visited[row][col]:
                queue.append(neighbor)
                visited[row][col] = True
                parent[row][col] = cell

    print("Nu există cale către destinație.")

def main():
    maze = [
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0]
    ]

    start = (0, 0)
    end = (4, 4)

    lee_algorithm(maze, start, end)

if __name__ == "__main__":
    main()

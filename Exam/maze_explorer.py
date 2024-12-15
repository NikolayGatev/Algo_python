from collections import deque

# Directions for moving in the maze (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def shortest_path(maze, n):
    # Find the start (S) and end (E) positions
    start = None
    end = None
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    # BFS setup
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.popleft()

        # If we reached the destination
        if (x, y) == end:
            return dist

        # Check all 4 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # If the new position is within bounds and is not a wall or visited
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    # In case there's no path, but as per problem constraints, this won't happen
    return -1


# Input reading
n = int(input())
maze = [input().strip() for _ in range(n)]

# Find the shortest path and print the result
print(shortest_path(maze, n))
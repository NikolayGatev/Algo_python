
def dfs(row, col, parent, matrix, visited):
    if not (0 <= row < len(matrix) and 0 <= col < len(matrix[0])):
        return
    if visited[row][col]:
        return
    if matrix[row][col] != parent:
        return

    visited[row][col] = True
    dfs(row - 1, col, parent, matrix, visited)
    dfs(row + 1, col, parent, matrix, visited)
    dfs(row, col - 1, parent, matrix, visited)
    dfs(row, col + 1, parent, matrix, visited)


rows = int(input())
cols = int(input())

matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

areas = {}
total_areas = 0

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]   
        dfs(row,col,key,matrix,visited)
        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1
        total_areas += 1
print(f'Areas: {total_areas}')
for area, size in sorted(areas.items()):
    print(f'Letter \'{area}\' -> {size}')
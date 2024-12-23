from collections import deque

def dfs(node, graph, visited, result):
    if node in visited:
        return
    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, result)

    result.appendleft(node)

graph = {}

while True:
    line = input()
    if line == 'End':
        break
    args = [x.strip() for x in line.split('->')]
    node = args[0]
    if len(args) == 1:
        graph[node] = []
    else:
        graph[node] = args[1].split()


visited = set()
result = deque()

for node in graph:
    dfs(node, graph, visited, result)

print(*result, sep=' ')
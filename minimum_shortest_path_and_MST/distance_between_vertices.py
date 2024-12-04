from collections import deque
from random import paretovariate

nodes = int(input())
pairs = int(input())

graph = {}

for _ in range(nodes):
    node_str, children_str = input().split(':')
    node = int(node_str)
    children = [int(x) for x in children_str.split()] if children_str else []
    graph[node] = children

for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]

    queue = deque([source])
    visited = {source}

    parent = {source: None}

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if child in visited:
                continue
            queue.append(child)
            visited.add(child)
            parent[child] = node
    if destination not in parent:
        print(f'{{{source}, {destination}}} -> -1')
        continue
    path = deque() # if keep path
    size = 0
    node = destination
    while node is not None:
        path.appendleft(node)
        node = parent[node]
        size += 1
    print(f'{{{source}, {destination}}} -> {len(path) - 1}')

    print(deque([4]))

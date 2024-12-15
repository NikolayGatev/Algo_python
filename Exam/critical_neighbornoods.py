import heapq


def find_shortest_path(roads, closed_roads, start_city, end_city):
    # Create the graph as an adjacency list
    graph = {}

    # Adding roads to the graph
    for road in roads:
        city1, city2, distance = road
        # Skip the closed roads
        if (city1, city2) not in closed_roads and (city2, city1) not in closed_roads:
            if city1 not in graph:
                graph[city1] = []
            if city2 not in graph:
                graph[city2] = []
            graph[city1].append((city2, distance))
            graph[city2].append((city1, distance))

    # Dijkstra's algorithm to find the shortest path
    # Priority queue for Dijkstra's algorithm
    pq = [(0, start_city)]  # (distance, city)
    distances = {start_city: 0}
    predecessors = {start_city: None}

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        if current_city == end_city:
            break

        for neighbor, weight in graph.get(current_city, []):
            new_distance = current_distance + weight
            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_city
                heapq.heappush(pq, (new_distance, neighbor))

    # Reconstruct the path
    path = []
    city = end_city
    while city is not None:
        path.append(city)
        city = predecessors[city]

    # Reverse the path to start from the start city
    path.reverse()

    return path, distances.get(end_city, -1)


# Input reading
r = int(input())  # number of roads
roads = []

for _ in range(r):
    road = input().strip().split(' - ')
    city1 = road[0]
    city2 = road[1]
    distance = int(road[2])
    roads.append((city1, city2, distance))

# Reading closed roads
closed_roads_input = input().strip()
closed_roads = set()

if closed_roads_input:
    closed_roads_list = closed_roads_input.split(',')
    for road in closed_roads_list:
        city1, city2 = road.split('-')
        closed_roads.add((city1, city2))

# Reading the start and end cities
start_city = input().strip()
end_city = input().strip()

# Find the shortest path
path, total_distance = find_shortest_path(roads, closed_roads, start_city, end_city)

# Print the result
print(' - '.join(path))
print(total_distance)
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def reconstruct_path(prev, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = prev[end]
    path.reverse()
    return path

graph = {
    0: [(1, 4), (7, 8)],
    1: [(0, 4), (2, 8), (7, 11)],
    2: [(1, 8), (3, 7), (8, 2), (5, 4)],
    3: [(2, 7), (4, 9), (5, 14)],
    4: [(3, 9), (5, 10)],
    5: [(4, 10), (3, 14), (2, 4), (6, 2)],
    6: [(5, 2), (7, 1), (8, 6)],
    7: [(0, 8), (1, 11), (6, 1), (8, 7)],
    8: [(2, 2), (6, 6), (7, 7)]
}

start_node = 0
distances, previous_nodes = dijkstra(graph, start_node)

print(f"Shortest distances from node {start_node}:")
for node in range(len(graph)):
    print(f"Node {node}: Distance = {distances[node]}")

print("\nPaths from node 0 to each node:")
for node in range(len(graph)):
    path = reconstruct_path(previous_nodes, start_node, node)
    print(f"Path to {node}: {' -> '.join(map(str, path))}")

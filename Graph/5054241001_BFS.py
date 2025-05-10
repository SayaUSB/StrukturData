from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(f"{node}")
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

def create_adjacency_list(nodes, edges):
    adj_list = {node: [] for node in nodes}
    
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  # Undirected graph
        
    return adj_list

# Graf Input
nodes = [0, 1, 2, 3, 4, 5, 6]
edges = [
    [0,1],
    [0,2],
    [1,2],
    [1,3],
    [2,4],
    [3,4],
    [4,5],
    [5,6]
]

adj_list = create_adjacency_list(nodes, edges)

# BFS from 0
bfs(adj_list, 0)

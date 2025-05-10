def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    print(f"{start}")
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

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

# DFS from 0
dfs(adj_list, 0)

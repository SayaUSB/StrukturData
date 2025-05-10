def create_adjacency_matrix(nodes, edges):
    n = len(nodes)
    matrix = [[0]*n for _ in range(n)]  # Awalnya semua nol
    node_index = {node: i for i, node in enumerate(nodes)}
    
    for u, v in edges:
        i = node_index[u]
        j = node_index[v]
        matrix[i][j] = 1
        matrix[j][i] = 1  # Undirected graph
        
    return matrix

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

adj_matrix = create_adjacency_matrix(nodes, edges)
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

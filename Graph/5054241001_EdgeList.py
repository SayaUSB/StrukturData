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

print("\nWeighted Edge List:")
for u, v, w in edges:
    print(f"{u} - {v} (Bobot: {w})")

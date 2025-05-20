import pygame
import time
import random

# ----------- Graph Setup -----------
nodes = {
    0: (100, 100),
    1: (300, 100),
    2: (500, 100),
    3: (200, 300),
    4: (400, 300)
}

edges = [
    (1, 0, 1),
    (3, 0, 3),
    (4, 1, 2),
    (2, 1, 3),
    (5, 2, 4),
    (1, 3, 4),
]

# ----------- Disjoint Set (Union Find) -----------
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[py] = px
        return True

# ----------- Pygame Setup -----------
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (0, 128, 255)
GREEN = (0, 200, 0)
GRAY  = (150, 150, 150)
RED   = (200, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kruskal's MST Animation")
font = pygame.font.SysFont(None, 24)

def draw_graph(mst_edges=[], highlight_edge=None):
    """Drawing helpers"""
    screen.fill(WHITE)

    # Draw all edges
    for w, u, v in edges:
        color = GRAY
        if (u, v) in mst_edges or (v, u) in mst_edges:
            color = GREEN
        if highlight_edge == (u, v) or highlight_edge == (v, u):
            color = RED
        pygame.draw.line(screen, color, nodes[u], nodes[v], 3)

        # Draw weight
        midx = (nodes[u][0] + nodes[v][0]) // 2
        midy = (nodes[u][1] + nodes[v][1]) // 2
        weight_text = font.render(str(w), True, BLACK)
        screen.blit(weight_text, (midx, midy))

    # Draw nodes
    for i, (x, y) in nodes.items():
        pygame.draw.circle(screen, BLUE, (x, y), 20)
        text = font.render(str(i), True, WHITE)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

    pygame.display.flip()

def kruskal_visual():
    """Kruskal Algorithm + Animation"""
    dsu = DSU(len(nodes))
    mst = []

    sorted_edges = sorted(edges)
    for w, u, v in sorted_edges:
        draw_graph(mst_edges=mst, highlight_edge=(u, v))
        time.sleep(1)  # Animation delay

        if dsu.union(u, v):
            mst.append((u, v))

        draw_graph(mst_edges=mst)
        time.sleep(0.5)

if __name__ == "__main__":
    draw_graph()
    running = True
    started = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not started:
                kruskal_visual()
                started = True
    pygame.quit()

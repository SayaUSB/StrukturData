import pygame
import time
import heapq

# ---------- Node dan Edge ----------
nodes = {
    0: (100, 100),
    1: (300, 100),
    2: (500, 100),
    3: (200, 300),
    4: (400, 300),
    5: (300, 250)
}

# Adjacency list: node -> (weight, neighbor)
graph = {
    0: [(1, 1), (3, 3)],
    1: [(0, 1), (2, 4), (3, 2)],
    2: [(1, 4), (4, 5), (5, 5)],
    3: [(0, 3), (1, 2), (4, 1)],
    4: [(2, 4), (3, 1), (5, 2)], 
    5: [(2, 5), (4, 2)]           
}

# ---------- Pygame Setup ----------
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (0, 128, 255)
GREEN = (0, 200, 0)
GRAY  = (150, 150, 150)
RED   = (200, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prim's MST Animation")
font = pygame.font.SysFont(None, 24)

# ---------- Drawing ----------
def draw_graph(mst_edges=[], highlight_edge=None):
    screen.fill(WHITE)

    # Draw all edges
    drawn = set()
    for u in graph:
        for w, v in graph[u]:
            if (u, v) in drawn or (v, u) in drawn:
                continue
            color = GRAY
            if (u, v) in mst_edges or (v, u) in mst_edges:
                color = GREEN
            if highlight_edge == (u, v) or highlight_edge == (v, u):
                color = RED
            pygame.draw.line(screen, color, nodes[u], nodes[v], 3)
            # Weight label
            midx = (nodes[u][0] + nodes[v][0]) // 2
            midy = (nodes[u][1] + nodes[v][1]) // 2
            text = font.render(str(w), True, BLACK)
            screen.blit(text, (midx, midy))
            drawn.add((u, v))

    # Draw nodes
    for i, (x, y) in nodes.items():
        pygame.draw.circle(screen, BLUE, (x, y), 20)
        text = font.render(str(i), True, WHITE)
        screen.blit(text, text.get_rect(center=(x, y)))

    pygame.display.flip()

def prim_visual(start=0):
    """Prim's Algorithm + Animation"""
    visited = set()
    mst = []
    pq = []

    visited.add(start)
    for w, v in graph[start]:
        heapq.heappush(pq, (w, start, v))

    while pq:
        w, u, v = heapq.heappop(pq)

        draw_graph(mst_edges=mst, highlight_edge=(u, v))
        time.sleep(1)

        if v not in visited:
            visited.add(v)
            mst.append((u, v))
            draw_graph(mst_edges=mst)
            time.sleep(0.5)

            for weight, neighbor in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, v, neighbor))

if __name__ == "__main__":
    draw_graph()
    running = True
    started = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not started:
                prim_visual(start=0)
                started = True
    pygame.quit()

import pygame
import math

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    return node.height if node else 0

def get_balance(node):
    return height(node.left) - height(node.right) if node else 0

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1
    return y

def insert(node, key):
    if not node:
        return Node(key)
    elif key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node

    node.height = 1 + max(height(node.left), height(node.right))
    balance = get_balance(node)

    if balance > 1 and key < node.left.key:
        return right_rotate(node)
    if balance < -1 and key > node.right.key:
        return left_rotate(node)
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

WIDTH, HEIGHT = 800, 600
NODE_RADIUS = 20
VERTICAL_SPACING = 80
FONT_SIZE = 20

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AVL Tree Visualization")
font = pygame.font.SysFont(None, FONT_SIZE)

def assign_positions(node, x, y, angle_range, depth=0):
    """Assign node positions recursively"""
    if not node:
        return
    node.x = x
    node.y = y

    angle = angle_range / 2
    offset = WIDTH // (2 ** (depth + 2))
    
    if node.left:
        assign_positions(node.left, x - offset, y + VERTICAL_SPACING, angle_range / 2, depth + 1)
    if node.right:
        assign_positions(node.right, x + offset, y + VERTICAL_SPACING, angle_range / 2, depth + 1)

def draw_tree(node):
    if not node:
        return
    if node.left:
        pygame.draw.line(screen, (0, 0, 0), (node.x, node.y), (node.left.x, node.left.y), 2)
    if node.right:
        pygame.draw.line(screen, (0, 0, 0), (node.x, node.y), (node.right.x, node.right.y), 2)
    
    draw_tree(node.left)
    draw_tree(node.right)
    
    pygame.draw.circle(screen, (0, 128, 255), (node.x, node.y), NODE_RADIUS)
    text = font.render(str(node.key), True, (255, 255, 255))
    text_rect = text.get_rect(center=(node.x, node.y))
    screen.blit(text, text_rect)

if __name__ == "__main__":
    root = None
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = insert(root, key)

    assign_positions(root, WIDTH // 2, 50, math.pi)

    running = True
    while running:
        screen.fill((255, 255, 255))
        draw_tree(root)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

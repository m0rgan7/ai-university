import heapq
from collections import deque
import copy
import os

# Constantes
GRID_SIZE = 15
START = (0, 0)
GOAL = (14, 14)
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Heuristica
def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Check if the cell is valid
def is_valid(x, y, grid):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and grid[x][y] == '.'

# Parse .txt file into grid
def load_map(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    grid = []
    for line in lines:
        parts = line.strip().split()
        row = list(parts[1])
        grid.append(row)
    return grid

# BFS algorithm
def bfs(grid):
    queue = deque()
    queue.append((START, [START]))
    visited = set()
    visited.add(START)
    nodes_explored = 0

    while queue:
        current, path = queue.popleft()
        nodes_explored += 1
        if current == GOAL:
            return path, nodes_explored
        for dx, dy in DIRS:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(nx, ny, grid) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    return None, nodes_explored

# A* algorithm
def a_star(grid):
    heap = []
    heapq.heappush(heap, (manhattan(START, GOAL), 0, START, [START]))
    visited = set()
    nodes_explored = 0

    while heap:
        est_total_cost, cost, current, path = heapq.heappop(heap)
        nodes_explored += 1
        if current == GOAL:
            return path, nodes_explored
        if current in visited:
            continue
        visited.add(current)
        for dx, dy in DIRS:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(nx, ny, grid) and (nx, ny) not in visited:
                new_cost = cost + 1
                priority = new_cost + manhattan((nx, ny), GOAL)
                heapq.heappush(heap, (priority, new_cost, (nx, ny), path + [(nx, ny)]))
    return None, nodes_explored

# Draw path on the map
def draw_path(grid, path):
    grid_copy = copy.deepcopy(grid)
    for x, y in path:
        if (x, y) not in [START, GOAL]:
            grid_copy[x][y] = '*'
    grid_copy[START[0]][START[1]] = 'S'
    grid_copy[GOAL[0]][GOAL[1]] = 'G'
    return grid_copy

def print_grid(grid):
    for row in grid:
        print(''.join(row))

# Run both algorithms
def run_algorithms(name, grid):
    print(f"\n=== {name} ===")
    
    bfs_path, bfs_nodes = bfs(grid)
    a_star_path, a_star_nodes = a_star(grid)

    print("\n[BFS]")
    if bfs_path:
        print(f"  ✅ Path found | Length: {len(bfs_path)-1} | Nodes explored: {bfs_nodes}")
    else:
        print(f"  ❌ No path found | Nodes explored: {bfs_nodes}")

    print("\n[A*]")
    if a_star_path:
        print(f"  ✅ Path found | Length: {len(a_star_path)-1} | Nodes explored: {a_star_nodes}")
    else:
        print(f"  ❌ No path found | Nodes explored: {a_star_nodes}")

    # Print maps with paths
    if bfs_path:
        print("\nMap with BFS Path:")
        print_grid(draw_path(grid, bfs_path))

    if a_star_path:
        print("\nMap with A* Path:")
        print_grid(draw_path(grid, a_star_path))

    # Compare
    if bfs_path and a_star_path:
        print("\n[Comparison]")
        print(f"  - Path length (BFS): {len(bfs_path)-1}")
        print(f"  - Path length (A*): {len(a_star_path)-1}")
        print(f"  - Nodes explored (BFS): {bfs_nodes}")
        print(f"  - Nodes explored (A*): {a_star_nodes}")
        if bfs_nodes > a_star_nodes:
            print("  ✅ A* was more efficient (fewer nodes explored)")
        elif bfs_nodes < a_star_nodes:
            print("  ✅ BFS was more efficient (fewer nodes explored)")
        else:
            print("  🔄 Both explored the same number of nodes")

# Run all maps
if __name__ == "__main__":
    map_folder = "maps"
    map_files = ["map_a.txt", "map_b.txt", "map_c.txt"]
    for filename in map_files:
        map_path = os.path.join(map_folder, filename)
        map_grid = load_map(map_path)
        run_algorithms(filename.upper(), map_grid)

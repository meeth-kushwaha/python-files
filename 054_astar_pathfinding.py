"""Program 054: A* Pathfinding on 2D Grid."""
import heapq

def astar(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
    rows, cols = len(grid), len(grid[0])
    pq = [(0 + abs(start[0]-end[0]) + abs(start[1]-end[1]), 0, start, [start])]
    visited = {}

    while pq:
        _, cost, curr, path = heapq.heappop(pq)
        if curr == end:
            return path
        if curr in visited and visited[curr] <= cost:
            continue
        visited[curr] = cost

        r, c = curr
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                h = abs(nr - end[0]) + abs(nc - end[1])
                heapq.heappush(pq, (cost + 1 + h, cost + 1, (nr, nc), path + [(nr, nc)]))
    return None

if __name__ == "__main__":
    print("--- 054: A* Pathfinding ---")
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    path = astar(grid, (0, 0), (4, 4))
    print(f"Path length: {len(path)} steps")
    print(f"Route: {path}")

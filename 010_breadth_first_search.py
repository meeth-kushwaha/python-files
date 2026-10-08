"""Program 010: Breadth-First Search (BFS) and Shortest Path."""
from collections import deque

def bfs_shortest_path(graph: dict[str, list[str]], start: str, goal: str) -> list[str] | None:
    queue = deque([[start]])
    visited = {start}
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

if __name__ == "__main__":
    print("--- 010: Breadth-First Search ---")
    network = {
        "Alice": ["Bob", "Claire", "Dennis"],
        "Bob": ["Alice", "Frank"],
        "Claire": ["Alice", "Dennis"],
        "Dennis": ["Alice", "Claire", "George"],
        "Frank": ["Bob", "George"],
        "George": ["Dennis", "Frank"]
    }
    path = bfs_shortest_path(network, "Alice", "George")
    print(f"Shortest path from Alice to George: {' -> '.join(path)}")

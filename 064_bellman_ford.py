"""Program 064: Bellman-Ford Shortest Path with Negative Cycle Detection."""
def bellman_ford(vertices: int, edges: list[tuple[int, int, int]], src: int):
    dist = [float("inf")] * vertices
    dist[src] = 0

    for _ in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative weight cycle!")
    return dist

if __name__ == "__main__":
    print("--- 064: Bellman-Ford ---")
    edges = [(0, 1, 4), (0, 2, 5), (1, 2, -3), (2, 3, 2)]
    d = bellman_ford(4, edges, 0)
    print("Shortest distances from 0:", d)

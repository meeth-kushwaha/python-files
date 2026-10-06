"""Program 006: Dijkstra's Shortest Path Algorithm on Weighted Graphs."""
import heapq

def dijkstra(graph: dict[str, list[tuple[str, int]]], start: str) -> dict[str, int]:
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distances[u]:
            continue
        for v, weight in graph.get(u, []):
            dist = curr_dist + weight
            if dist < distances[v]:
                distances[v] = dist
                heapq.heappush(pq, (dist, v))
    return distances

if __name__ == "__main__":
    print("--- 006: Dijkstra Shortest Path ---")
    g = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2)],
        "E": [("C", 10), ("D", 2)]
    }
    dist = dijkstra(g, "A")
    for dest, cost in dist.items():
        print(f"Shortest path A -> {dest}: {cost}")

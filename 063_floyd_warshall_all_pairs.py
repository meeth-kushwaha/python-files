"""Program 063: Floyd-Warshall All-Pairs Shortest Path."""
def floyd_warshall(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)
    dist = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

if __name__ == "__main__":
    print("--- 063: Floyd-Warshall ---")
    INF = float("inf")
    graph = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]
    res = floyd_warshall(graph)
    print("Distance Matrix:")
    for r in res:
        print([int(x) if x != INF else "INF" for x in r])

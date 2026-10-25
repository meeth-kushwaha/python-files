"""Program 061: Kahn's Algorithm for Topological Sort."""
from collections import deque

def topological_sort(num_nodes: int, edges: list[tuple[int, int]]) -> list[int]:
    adj = {i: [] for i in range(num_nodes)}
    in_degree = [0] * num_nodes
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) != num_nodes:
        raise ValueError("Graph has at least one cycle!")
    return order

if __name__ == "__main__":
    print("--- 061: Topological Sort ---")
    # Build dependencies: 5->2, 5->0, 4->0, 4->1, 2->3, 3->1
    tasks = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    print("Topological Task Order:", topological_sort(6, tasks))

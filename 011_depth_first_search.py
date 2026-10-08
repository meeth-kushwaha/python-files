"""Program 011: Depth-First Search (DFS) & Cycle Detection in Directed Graph."""
def has_cycle(graph: dict[str, list[str]]) -> bool:
    visited = set()
    rec_stack = set()

    def dfs(node: str) -> bool:
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

if __name__ == "__main__":
    print("--- 011: Depth-First Search Cycle Detection ---")
    g_cyclic = {"A": ["B"], "B": ["C"], "C": ["A"]}
    g_acyclic = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    print(f"g_cyclic has cycle: {has_cycle(g_cyclic)}")
    print(f"g_acyclic has cycle: {has_cycle(g_acyclic)}")

"""Program 062: Disjoint Set Union (DSU / Union-Find)."""
class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

if __name__ == "__main__":
    print("--- 062: Disjoint Set Union ---")
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    print("0 connected to 2?", uf.find(0) == uf.find(2))
    print("0 connected to 3?", uf.find(0) == uf.find(3))

"""Program 056: K-Means 2D Clustering Algorithm."""
import random

def dist_sq(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def k_means(points: list[tuple[float, float]], k: int, iters: int = 20):
    centroids = random.sample(points, k)
    for _ in range(iters):
        clusters = [[] for _ in range(k)]
        for p in points:
            closest = min(range(k), key=lambda idx: dist_sq(p, centroids[idx]))
            clusters[closest].append(p)
        # Update
        for i in range(k):
            if clusters[i]:
                avg_x = sum(p[0] for p in clusters[i]) / len(clusters[i])
                avg_y = sum(p[1] for p in clusters[i]) / len(clusters[i])
                centroids[i] = (avg_x, avg_y)
    return centroids, clusters

if __name__ == "__main__":
    print("--- 056: K-Means Clustering ---")
    data = [(1.0, 1.0), (1.5, 2.0), (2.0, 1.0), (8.0, 8.0), (9.0, 7.5), (8.5, 9.0)]
    centers, clusters = k_means(data, k=2)
    print("Centroid 1:", centers[0], "Points count:", len(clusters[0]))
    print("Centroid 2:", centers[1], "Points count:", len(clusters[1]))

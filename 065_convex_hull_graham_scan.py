"""Program 065: Graham Scan 2D Convex Hull."""
def orientation(p: tuple[int, int], q: tuple[int, int], r: tuple[int, int]) -> int:
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2 # Clockwise or Counterclockwise

def convex_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts
    # Build lower hull
    lower = []
    for p in pts:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) != 2:
            lower.pop()
        lower.append(p)
    # Build upper hull
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) != 2:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

if __name__ == "__main__":
    print("--- 065: Convex Hull Graham Scan ---")
    pts = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
    hull = convex_hull(pts)
    print("Convex Hull Vertices:", hull)

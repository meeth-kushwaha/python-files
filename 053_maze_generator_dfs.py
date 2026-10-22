"""Program 053: Randomized DFS 2D Maze Generator."""
import random

def generate_maze(width: int = 15, height: int = 11) -> list[list[str]]:
    # Odd dimensions
    w, h = width | 1, height | 1
    grid = [["#"] * w for _ in range(h)]

    def carve(cx: int, cy: int):
        grid[cy][cx] = " "
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] == "#":
                grid[cy + dy // 2][cx + dx // 2] = " "
                carve(nx, ny)

    carve(1, 1)
    grid[1][0] = "S" # Start
    grid[h - 2][w - 1] = "E" # End
    return grid

if __name__ == "__main__":
    print("--- 053: Maze Generator ---")
    maze = generate_maze(15, 9)
    for row in maze:
        print("".join(row))

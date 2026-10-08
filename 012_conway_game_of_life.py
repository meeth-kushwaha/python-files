"""Program 012: Conway's Game of Life Cellular Automaton."""
def step_life(grid: list[list[int]]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            neighbors = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        neighbors += grid[nr][nc]
            
            if grid[r][c] == 1 and neighbors in (2, 3):
                new_grid[r][c] = 1
            elif grid[r][c] == 0 and neighbors == 3:
                new_grid[r][c] = 1
    return new_grid

def render(grid: list[list[int]]) -> str:
    return "\n".join("".join(" #"[cell] for cell in row) for row in grid)

if __name__ == "__main__":
    print("--- 012: Conway's Game of Life (Blinker Oscillator) ---")
    # Blinker
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    print("Initial state:")
    print(render(grid))
    print("\nNext generation:")
    print(render(step_life(grid)))

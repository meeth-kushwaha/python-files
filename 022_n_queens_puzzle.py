"""Program 022: N-Queens Problem Solver."""
def solve_n_queens(n: int) -> list[list[str]]:
    solutions = []
    cols = set()
    diag_pos = set() # r + c
    diag_neg = set() # r - c
    board = [["."] * n for _ in range(n)]

    def backtrack(r: int):
        if r == n:
            solutions.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r + c) in diag_pos or (r - c) in diag_neg:
                continue
            cols.add(c)
            diag_pos.add(r + c)
            diag_neg.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            cols.remove(c)
            diag_pos.remove(r + c)
            diag_neg.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return solutions

if __name__ == "__main__":
    print("--- 022: N-Queens Puzzle (N=4) ---")
    solutions = solve_n_queens(4)
    print(f"Found {len(solutions)} distinct solutions for 4-Queens.")
    for i, sol in enumerate(solutions, 1):
        print(f"Solution #{i}:")
        for line in sol:
            print("  " + line)

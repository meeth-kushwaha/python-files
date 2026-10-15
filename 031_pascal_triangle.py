"""Program 031: Pascal's Triangle & Binomial Coefficients."""
def generate_pascal_triangle(n_rows: int) -> list[list[int]]:
    triangle = []
    for r in range(n_rows):
        row = [1] * (r + 1)
        for c in range(1, r):
            row[c] = triangle[r - 1][c - 1] + triangle[r - 1][c]
        triangle.append(row)
    return triangle

def format_triangle(tri: list[list[int]]) -> str:
    lines = []
    max_w = len(" ".join(map(str, tri[-1])))
    for row in tri:
        line_str = " ".join(map(str, row))
        lines.append(line_str.center(max_w))
    return "\n".join(lines)

if __name__ == "__main__":
    print("--- 031: Pascal's Triangle ---")
    tri = generate_pascal_triangle(7)
    print(format_triangle(tri))

"""Program 095: Matrix Determinant via Gaussian Elimination."""
def matrix_determinant(matrix: list[list[float]]) -> float:
    n = len(matrix)
    a = [row[:] for row in matrix]
    det = 1.0
    for i in range(n):
        pivot = i
        for r in range(i + 1, n):
            if abs(a[r][i]) > abs(a[pivot][i]):
                pivot = r
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            det = -det
        if abs(a[i][i]) < 1e-12:
            return 0.0
        det *= a[i][i]
        for r in range(i + 1, n):
            factor = a[r][i] / a[i][i]
            for c in range(i + 1, n):
                a[r][c] -= factor * a[i][c]
    return round(det, 4)

if __name__ == "__main__":
    print("--- 095: Matrix Determinant ---")
    m = [
        [6.0, 1.0, 1.0],
        [4.0, -2.0, 5.0],
        [2.0, 8.0, 7.0]
    ]
    print("Determinant of M:", matrix_determinant(m))

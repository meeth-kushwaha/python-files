"""Program 017: Pure Python Matrix Operations (Add, Multiply, Transpose)."""
Matrix = list[list[float]]

def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def mat_mult(a: Matrix, b: Matrix) -> Matrix:
    r_a, c_a = len(a), len(a[0])
    r_b, c_b = len(b), len(b[0])
    if c_a != r_b:
        raise ValueError("Incompatible dimensions for multiplication")
    res = [[0.0] * c_b for _ in range(r_a)]
    for i in range(r_a):
        for j in range(c_b):
            res[i][j] = sum(a[i][k] * b[k][j] for k in range(c_a))
    return res

def mat_transpose(a: Matrix) -> Matrix:
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

if __name__ == "__main__":
    print("--- 017: Matrix Operations ---")
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    print(f"Addition:\n{mat_add(m1, m2)}")
    print(f"Multiplication:\n{mat_mult(m1, m2)}")
    print(f"Transpose of M1:\n{mat_transpose(m1)}")

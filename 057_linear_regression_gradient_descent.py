"""Program 057: Simple Linear Regression using Gradient Descent."""
def linear_regression(x: list[float], y: list[float], lr: float = 0.01, epochs: int = 1000):
    m, b = 0.0, 0.0
    n = len(x)
    for _ in range(epochs):
        dm = (-2 / n) * sum(x[i] * (y[i] - (m * x[i] + b)) for i in range(n))
        db = (-2 / n) * sum(y[i] - (m * x[i] + b) for i in range(n))
        m -= lr * dm
        b -= lr * db
    return m, b

if __name__ == "__main__":
    print("--- 057: Linear Regression ---")
    # y = 2x + 1 with some points
    xs = [1.0, 2.0, 3.0, 4.0, 5.0]
    ys = [3.0, 5.0, 7.0, 9.0, 11.0]
    slope, intercept = linear_regression(xs, ys)
    print(f"Fitted Line: y = {slope:.2f}x + {intercept:.2f}")

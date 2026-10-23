"""Program 055: Single-Layer Perceptron for Logic Gates."""
class Perceptron:
    def __init__(self, num_inputs: int, lr: float = 0.1, epochs: int = 100):
        self.weights = [0.0] * num_inputs
        self.bias = 0.0
        self.lr = lr
        self.epochs = epochs

    def predict(self, x: list[float]) -> int:
        activation = sum(w * xi for w, xi in zip(self.weights, x)) + self.bias
        return 1 if activation >= 0 else 0

    def fit(self, X: list[list[float]], y: list[int]):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                pred = self.predict(xi)
                error = target - pred
                for j in range(len(self.weights)):
                    self.weights[j] += self.lr * error * xi[j]
                self.bias += self.lr * error

if __name__ == "__main__":
    print("--- 055: Perceptron Classifier (AND Gate) ---")
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [0, 0, 0, 1]
    p = Perceptron(2)
    p.fit(X, y)
    for sample in X:
        print(f"Input {sample} -> Output {p.predict(sample)}")

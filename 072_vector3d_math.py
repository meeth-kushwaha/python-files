"""Program 072: 3D Vector Math Library."""
import math

class Vector3D:
    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

if __name__ == "__main__":
    print("--- 072: 3D Vector Math ---")
    v1 = Vector3D(1, 0, 0)
    v2 = Vector3D(0, 1, 0)
    print("v1 x v2:", v1.cross(v2))
    print("Magnitude of (3,4,0):", Vector3D(3, 4, 0).magnitude())

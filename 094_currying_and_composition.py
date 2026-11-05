"""Program 094: Functional Programming: Compose & Currying."""
from functools import reduce

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def pipe(val, *functions):
    return reduce(lambda x, f: f(x), functions, val)

def curry2(f):
    return lambda a: lambda b: f(a, b)

if __name__ == "__main__":
    print("--- 094: Functional Compose & Currying ---")
    add_ten = lambda x: x + 10
    double = lambda x: x * 2
    to_str = lambda x: f"Value: {x}"

    pipeline = compose(to_str, double, add_ten)
    print(pipeline(5)) # (5 + 10) * 2 = 30 -> "Value: 30"

    multiply = curry2(lambda a, b: a * b)
    triple = multiply(3)
    print("Curried triple of 7:", triple(7))

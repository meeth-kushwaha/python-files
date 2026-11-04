"""Program 093: Custom Float-Capable Range Generator."""
def float_range(start: float, stop: float = None, step: float = 1.0):
    if stop is None:
        start, stop = 0.0, float(start)
    else:
        start, stop = float(start), float(stop)
    step = float(step)
    if step == 0.0:
        raise ValueError("Step cannot be zero.")

    curr = start
    if step > 0:
        while curr < stop - 1e-9:
            yield round(curr, 8)
            curr += step
    else:
        while curr > stop + 1e-9:
            yield round(curr, 8)
            curr += step

if __name__ == "__main__":
    print("--- 093: Float Range Generator ---")
    print("Range [0.0 to 1.0 step 0.2]:", list(float_range(0.0, 1.0, 0.2)))
    print("Range [5.0 to 3.0 step -0.5]:", list(float_range(5.0, 3.0, -0.5)))

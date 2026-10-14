"""Program 030: ASCII Mandelbrot Fractal Generator."""
def mandelbrot(c: complex, max_iter: int) -> int:
    z = 0j
    for i in range(max_iter):
        if abs(z) > 2.0:
            return i
        z = z * z + c
    return max_iter

def render_ascii_mandelbrot(width: int = 60, height: int = 24, max_iter: int = 30) -> str:
    palette = " .:-=+*#%@"
    lines = []
    for y in range(height):
        row = []
        im = -1.2 + (y / height) * 2.4
        for x in range(width):
            re = -2.0 + (x / width) * 2.5
            iters = mandelbrot(complex(re, im), max_iter)
            idx = int((iters / max_iter) * (len(palette) - 1))
            row.append(palette[idx])
        lines.append("".join(row))
    return "\n".join(lines)

if __name__ == "__main__":
    print("--- 030: Mandelbrot ASCII Fractal ---")
    print(render_ascii_mandelbrot(50, 18, 25))

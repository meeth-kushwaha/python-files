"""Program 080: Terminal ASCII Bar Chart & Sparkline Plotter."""
import sys

# Ensure UTF-8 output encoding on Windows if supported
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def render_bar_chart(data: dict[str, float], max_width: int = 30) -> str:
    lines = []
    max_val = max(data.values()) if data else 1.0
    for label, val in data.items():
        bar_len = int((val / max_val) * max_width)
        bar = "#" * bar_len
        lines.append(f"{label:>10} | {bar:<{max_width}} {val}")
    return "\n".join(lines)

def render_sparkline(values: list[float]) -> str:
    ticks = "_.-~*#"
    min_v, max_v = min(values), max(values)
    rng = max(1e-9, max_v - min_v)
    return "".join(ticks[int(((v - min_v) / rng) * (len(ticks) - 1))] for v in values)

if __name__ == "__main__":
    print("--- 080: ASCII Chart Plotter ---")
    data = {"Sales": 120, "Marketing": 85, "R&D": 150, "Support": 60}
    print(render_bar_chart(data))
    print("\nTrend Sparkline:", render_sparkline([10, 25, 40, 30, 60, 85, 70, 95]))

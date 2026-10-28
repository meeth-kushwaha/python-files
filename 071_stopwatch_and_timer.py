"""Program 071: High-Resolution Stopwatch and Lap Tracker."""
import time

class Stopwatch:
    def __init__(self):
        self._start_time = None
        self._laps = []

    def start(self):
        self._start_time = time.perf_counter()
        self._laps.clear()

    def lap(self) -> float:
        if self._start_time is None:
            raise RuntimeError("Stopwatch not started.")
        curr = time.perf_counter()
        elapsed = curr - self._start_time
        self._laps.append(elapsed)
        return elapsed

if __name__ == "__main__":
    print("--- 071: Stopwatch & Lap Tracker ---")
    sw = Stopwatch()
    sw.start()
    time.sleep(0.01)
    lap1 = sw.lap()
    time.sleep(0.01)
    lap2 = sw.lap()
    print(f"Lap 1: {lap1*1000:.2f} ms")
    print(f"Lap 2: {lap2*1000:.2f} ms")

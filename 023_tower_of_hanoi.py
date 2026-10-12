"""Program 023: Tower of Hanoi Recursive Solver with Move Tracking."""
def hanoi(n: int, source: str, target: str, auxiliary: str, moves: list[str]):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target, moves)
        moves.append(f"Move disk {n} from {source} -> {target}")
        hanoi(n - 1, auxiliary, target, source, moves)

if __name__ == "__main__":
    print("--- 023: Tower of Hanoi (3 disks) ---")
    moves_log = []
    hanoi(3, "Peg A", "Peg C", "Peg B", moves_log)
    print(f"Total moves: {len(moves_log)} (Expected: 2^3 - 1 = 7)")
    for step in moves_log:
        print(" ", step)

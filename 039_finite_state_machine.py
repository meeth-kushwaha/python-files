"""Program 039: Finite State Machine (FSM) Turnstile Model."""
class TurnstileFSM:
    def __init__(self):
        self.state = "LOCKED"

    def coin(self):
        if self.state == "LOCKED":
            self.state = "UNLOCKED"
            return "Unlocked. Please push."
        return "Coin returned. Already unlocked."

    def push(self):
        if self.state == "UNLOCKED":
            self.state = "LOCKED"
            return "Pushed through. Now locked."
        return "Blocked! Turnstile is locked. Insert coin."

if __name__ == "__main__":
    print("--- 039: Finite State Machine ---")
    ts = TurnstileFSM()
    print("1. Action push:", ts.push())
    print("2. Action coin:", ts.coin())
    print("3. Action push:", ts.push())

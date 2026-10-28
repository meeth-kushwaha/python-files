"""Program 070: Personal Expense Tracker."""
from collections import defaultdict

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount: float, category: str, note: str):
        self.expenses.append({"amount": amount, "category": category, "note": note})

    def total(self) -> float:
        return sum(e["amount"] for e in self.expenses)

    def summary_by_category(self) -> dict[str, float]:
        summary = defaultdict(float)
        for e in self.expenses:
            summary[e["category"]] += e["amount"]
        return dict(summary)

if __name__ == "__main__":
    print("--- 070: Expense Tracker ---")
    tracker = ExpenseTracker()
    tracker.add_expense(45.50, "Groceries", "Supermarket")
    tracker.add_expense(12.00, "Transport", "Bus pass")
    tracker.add_expense(85.00, "Groceries", "Weekly shop")
    print(f"Total spent: ${tracker.total():.2f}")
    print(f"By category: {tracker.summary_by_category()}")

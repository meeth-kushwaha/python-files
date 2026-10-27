"""Program 069: CLI Todo List Manager."""
class TodoManager:
    def __init__(self):
        self.tasks = []

    def add(self, title: str, priority: str = "Medium"):
        self.tasks.append({"title": title, "priority": priority, "done": False})

    def complete(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True

    def list_all(self) -> list[str]:
        output = []
        for i, t in enumerate(self.tasks):
            status = "[x]" if t["done"] else "[ ]"
            output.append(f"{i}. {status} ({t['priority']}) {t['title']}")
        return output

if __name__ == "__main__":
    print("--- 069: CLI Todo Manager ---")
    mgr = TodoManager()
    mgr.add("Write unit tests", "High")
    mgr.add("Refactor database schema", "Medium")
    mgr.complete(0)
    for line in mgr.list_all():
        print(line)

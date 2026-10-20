"""Program 047: Command Pattern with Undo and Redo History."""
class TextEditor:
    def __init__(self):
        self.content = ""

class WriteCommand:
    def __init__(self, editor: TextEditor, text: str):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.content += self.text

    def undo(self):
        self.editor.content = self.editor.content[:-len(self.text)]

class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def execute(self, cmd):
        cmd.execute()
        self.undo_stack.append(cmd)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            cmd = self.undo_stack.pop()
            cmd.undo()
            self.redo_stack.append(cmd)

    def redo(self):
        if self.redo_stack:
            cmd = self.redo_stack.pop()
            cmd.execute()
            self.undo_stack.append(cmd)

if __name__ == "__main__":
    print("--- 047: Command Undo/Redo ---")
    ed = TextEditor()
    mgr = CommandManager()
    mgr.execute(WriteCommand(ed, "Hello "))
    mgr.execute(WriteCommand(ed, "World!"))
    print(f"After typing: '{ed.content}'")
    mgr.undo()
    print(f"After undo:   '{ed.content}'")
    mgr.redo()
    print(f"After redo:   '{ed.content}'")

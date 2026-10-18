"""Program 041: Factory Method Design Pattern."""
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class WindowsButton(Button):
    def render(self) -> str:
        return "[Windows Fluent Button]"

class MacButton(Button):
    def render(self) -> str:
        return "(macOS Rounded Button)"

class DialogFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

class WindowsDialog(DialogFactory):
    def create_button(self) -> Button:
        return WindowsButton()

class MacDialog(DialogFactory):
    def create_button(self) -> Button:
        return MacButton()

if __name__ == "__main__":
    print("--- 041: Factory Pattern ---")
    for factory in [WindowsDialog(), MacDialog()]:
        btn = factory.create_button()
        print(f"Rendered: {btn.render()}")

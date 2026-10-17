"""Program 038: Publish-Subscribe Event Emitter."""
from collections import defaultdict
from typing import Callable

class EventEmitter:
    def __init__(self):
        self._events: dict[str, list[Callable]] = defaultdict(list)

    def on(self, event_name: str, listener: Callable):
        self._events[event_name].append(listener)

    def emit(self, event_name: str, *args, **kwargs):
        for listener in list(self._events.get(event_name, [])):
            listener(*args, **kwargs)

    def off(self, event_name: str, listener: Callable):
        if listener in self._events.get(event_name, []):
            self._events[event_name].remove(listener)

if __name__ == "__main__":
    print("--- 038: Event Emitter Pub/Sub ---")
    bus = EventEmitter()
    def on_login(user):
        print(f"Notification: User '{user}' has logged in.")
    bus.on("login", on_login)
    bus.emit("login", "Dave")

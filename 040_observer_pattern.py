"""Program 040: Classic Observer Pattern."""
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message: str):
        for obs in self._observers:
            obs.update(message)

class Subscriber:
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f"[{self.name}] Received update: '{message}'")

if __name__ == "__main__":
    print("--- 040: Observer Pattern ---")
    news_channel = Subject()
    sub1 = Subscriber("Alice")
    sub2 = Subscriber("Bob")
    news_channel.attach(sub1)
    news_channel.attach(sub2)
    news_channel.notify("Breaking News: Python 3.14 Released!")

"""Program 099: Vector Clock for Distributed Causality Tracking."""
class VectorClock:
    def __init__(self, node_id: str, nodes: list[str]):
        self.node_id = node_id
        self.clock = {n: 0 for n in nodes}

    def tick(self):
        self.clock[self.node_id] += 1

    def send_event(self) -> dict[str, int]:
        self.tick()
        return dict(self.clock)

    def receive_event(self, incoming_clock: dict[str, int]):
        for node, val in incoming_clock.items():
            self.clock[node] = max(self.clock.get(node, 0), val)
        self.tick()

    def __repr__(self):
        return f"{self.node_id}: {dict(self.clock)}"

if __name__ == "__main__":
    print("--- 099: Vector Clocks ---")
    nodes = ["NodeA", "NodeB"]
    va = VectorClock("NodeA", nodes)
    vb = VectorClock("NodeB", nodes)

    va.tick()
    msg = va.send_event()
    vb.receive_event(msg)
    print(va)
    print(vb)

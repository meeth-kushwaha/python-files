"""Program 046: Chain of Responsibility Pattern."""
class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request: str) -> str:
        if self.successor:
            return self.successor.handle(request)
        return "No handler could process the request."

class SpamFilter(Handler):
    def handle(self, request: str) -> str:
        if "free cash" in request.lower():
            return "SpamFilter: Flagged as spam."
        return super().handle(request)

class AuthCheck(Handler):
    def handle(self, request: str) -> str:
        if "unauthorized" in request.lower():
            return "AuthCheck: Denied access."
        return super().handle(request)

if __name__ == "__main__":
    print("--- 046: Chain of Responsibility ---")
    chain = SpamFilter(AuthCheck())
    print(chain.handle("Win free cash now!"))
    print(chain.handle("Unauthorized request to secret resource"))
    print(chain.handle("Normal request payload"))

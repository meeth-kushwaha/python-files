"""Program 067: URL Shortener Engine with Base62 ID Encoding."""
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class URLShortener:
    def __init__(self, domain: str = "https://sho.rt/"):
        self.domain = domain
        self.counter = 1000
        self.url_map = {}
        self.id_map = {}

    def _encode_id(self, num: int) -> str:
        s = []
        while num > 0:
            s.append(ALPHABET[num % 62])
            num //= 62
        return "".join(reversed(s))

    def shorten(self, url: str) -> str:
        if url in self.url_map:
            return self.domain + self.url_map[url]
        code = self._encode_id(self.counter)
        self.counter += 1
        self.url_map[url] = code
        self.id_map[code] = url
        return self.domain + code

    def expand(self, short_url: str) -> str | None:
        code = short_url.replace(self.domain, "")
        return self.id_map.get(code)

if __name__ == "__main__":
    print("--- 067: URL Shortener Engine ---")
    engine = URLShortener()
    short = engine.shorten("https://docs.python.org/3/library/")
    print("Shortened URL:", short)
    print("Expanded URL: ", engine.expand(short))

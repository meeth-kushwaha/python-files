"""Program 087: Morse Code Encoder & Decoder."""
MORSE_MAP = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '0': '-----', ' ': '/'
}
REVERSE_MORSE = {v: k for k, v in MORSE_MAP.items()}

def encode_morse(text: str) -> str:
    return " ".join(MORSE_MAP.get(c.upper(), "?") for c in text)

def decode_morse(code: str) -> str:
    return "".join(REVERSE_MORSE.get(token, "?") for token in code.split(" "))

if __name__ == "__main__":
    print("--- 087: Morse Code ---")
    msg = "SOS HELP"
    encoded = encode_morse(msg)
    decoded = decode_morse(encoded)
    print(f"Message: {msg}")
    print(f"Morse:   {encoded}")
    print(f"Decoded: {decoded}")

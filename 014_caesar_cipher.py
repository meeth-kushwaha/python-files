"""Program 014: Caesar Cipher Encryptor, Decryptor, and Brute-Force Cracker."""
def caesar_cipher(text: str, shift: int) -> str:
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return "".join(result)

def crack_caesar(ciphertext: str) -> list[tuple[int, str]]:
    candidates = []
    for shift in range(1, 26):
        candidates.append((shift, caesar_cipher(ciphertext, -shift)))
    return candidates

if __name__ == "__main__":
    print("--- 014: Caesar Cipher ---")
    secret = "Python programming is awesome!"
    encrypted = caesar_cipher(secret, 7)
    print(f"Encrypted (+7): {encrypted}")
    print(f"Decrypted (-7): {caesar_cipher(encrypted, -7)}")

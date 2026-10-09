"""Program 015: Polyalphabetic Vigenère Cipher."""
def vigenere(text: str, key: str, decrypt: bool = False) -> str:
    res = []
    key_shifts = [ord(k.lower()) - ord('a') for k in key if k.isalpha()]
    k_idx = 0
    
    for ch in text:
        if ch.isalpha():
            shift = key_shifts[k_idx % len(key_shifts)]
            if decrypt:
                shift = -shift
            base = ord('A') if ch.isupper() else ord('a')
            res.append(chr((ord(ch) - base + shift) % 26 + base))
            k_idx += 1
        else:
            res.append(ch)
    return "".join(res)

if __name__ == "__main__":
    print("--- 015: Vigenere Cipher ---")
    msg = "ATTACK AT DAWN"
    k = "LEMON"
    enc = vigenere(msg, k)
    dec = vigenere(enc, k, decrypt=True)
    print(f"Original:  {msg}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")

"""Program 016: Educational RSA Toy Cryptosystem."""
def egcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = egcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modinv(a: int, m: int) -> int:
    gcd, x, _ = egcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

def generate_keypair(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    # For small primes test e=3 or 17
    for cand in [17, 65537, 3, 7]:
        if phi % cand != 0 and egcd(cand, phi)[0] == 1:
            e = cand
            break
    d = modinv(e, phi)
    return ((e, n), (d, n))

if __name__ == "__main__":
    print("--- 016: RSA Toy Cryptosystem ---")
    p, q = 61, 53
    public_key, private_key = generate_keypair(p, q)
    print(f"Public Key (e, n):  {public_key}")
    print(f"Private Key (d, n): {private_key}")
    
    msg_num = 42
    enc = pow(msg_num, public_key[0], public_key[1])
    dec = pow(enc, private_key[0], private_key[1])
    print(f"Original message:  {msg_num}")
    print(f"Encrypted message: {enc}")
    print(f"Decrypted message: {dec}")

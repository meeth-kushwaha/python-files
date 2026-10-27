"""Program 068: Password Strength & Entropy Analyzer."""
import math
import re

def analyze_password(password: str) -> dict:
    pool_size = 0
    if re.search(r"[a-z]", password):
        pool_size += 26
    if re.search(r"[A-Z]", password):
        pool_size += 26
    if re.search(r"[0-9]", password):
        pool_size += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        pool_size += 32

    entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0
    if entropy < 36:
        rating = "Very Weak"
    elif entropy < 60:
        rating = "Moderate"
    elif entropy < 80:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return {"length": len(password), "entropy_bits": round(entropy, 2), "rating": rating}

if __name__ == "__main__":
    print("--- 068: Password Strength Analyzer ---")
    for pwd in ["pass", "Password123!", "K9#m$L2!zQ8@vN"]:
        print(f"'{pwd}' -> {analyze_password(pwd)}")

"""Program 097: Pure Python RFC-4122 Compliant UUIDv4 Generator."""
import secrets

def generate_uuid4() -> str:
    raw_bytes = bytearray(secrets.token_bytes(16))
    # Version 4: set bits 12-15 of time_hi_and_version to 0100
    raw_bytes[6] = (raw_bytes[6] & 0x0f) | 0x40
    # Variant RFC 4122: set bits 6-7 of clock_seq_hi_and_reserved to 10
    raw_bytes[8] = (raw_bytes[8] & 0x3f) | 0x80

    hex_str = raw_bytes.hex()
    return f"{hex_str[0:8]}-{hex_str[8:12]}-{hex_str[12:16]}-{hex_str[16:20]}-{hex_str[20:32]}"

if __name__ == "__main__":
    print("--- 097: UUIDv4 Generator ---")
    for _ in range(3):
        print("Generated UUID:", generate_uuid4())

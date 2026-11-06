"""Program 098: Pure Python CRC32 Checksum Calculator."""
def crc32_checksum(data: bytes) -> int:
    crc = 0xFFFFFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            mask = -(crc & 1)
            crc = (crc >> 1) ^ (0xEDB88320 & mask)
    return ~crc & 0xFFFFFFFF

if __name__ == "__main__":
    print("--- 098: CRC32 Checksum Calculator ---")
    text = b"The quick brown fox jumps over the lazy dog"
    checksum = crc32_checksum(text)
    print(f"CRC-32 of test string: 0x{checksum:08X}")

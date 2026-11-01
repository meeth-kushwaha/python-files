"""Program 082: Low-Level Binary Buffer Packer & Unpacker."""
import struct

def pack_record(user_id: int, score: float, active: bool, tag: str) -> bytes:
    tag_bytes = tag.encode("utf-8")[:8].ljust(8, b"\x00")
    # Format: uint32, float32, bool (uint8), 8-byte string
    return struct.pack("!If?8s", user_id, score, active, tag_bytes)

def unpack_record(data: bytes) -> tuple:
    user_id, score, active, tag_bytes = struct.unpack("!If?8s", data)
    tag = tag_bytes.rstrip(b"\x00").decode("utf-8")
    return user_id, round(score, 2), active, tag

if __name__ == "__main__":
    print("--- 082: Binary Packer & Unpacker ---")
    packed = pack_record(1024, 98.75, True, "ADMIN")
    print(f"Packed size: {len(packed)} bytes, Hex: {packed.hex()}")
    unpacked = unpack_record(packed)
    print("Unpacked record:", unpacked)

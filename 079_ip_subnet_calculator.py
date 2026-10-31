"""Program 079: IPv4 CIDR Subnet Calculator."""
def ip_to_int(ip: str) -> int:
    octets = [int(x) for x in ip.split(".")]
    return (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]

def int_to_ip(val: int) -> str:
    return ".".join(str((val >> (8 * i)) & 255) for i in reversed(range(4)))

def calculate_subnet(cidr: str) -> dict:
    ip_str, prefix_len = cidr.split("/")
    prefix = int(prefix_len)
    mask = ((1 << 32) - 1) ^ ((1 << (32 - prefix)) - 1)
    ip_num = ip_to_int(ip_str)
    net_num = ip_num & mask
    bcast_num = net_num | (~mask & 0xFFFFFFFF)
    total_hosts = max(0, (1 << (32 - prefix)) - 2)

    return {
        "network": int_to_ip(net_num),
        "broadcast": int_to_ip(bcast_num),
        "netmask": int_to_ip(mask),
        "usable_hosts": total_hosts,
        "first_host": int_to_ip(net_num + 1) if total_hosts else None,
        "last_host": int_to_ip(bcast_num - 1) if total_hosts else None
    }

if __name__ == "__main__":
    print("--- 079: IPv4 Subnet Calculator ---")
    info = calculate_subnet("192.168.10.45/24")
    for k, v in info.items():
        print(f"{k}: {v}")

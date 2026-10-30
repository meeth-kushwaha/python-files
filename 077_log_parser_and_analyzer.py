"""Program 077: Web Server Log Parser & Analyzer."""
import re
from collections import Counter

LOG_PATTERN = re.compile(r'(?P<ip>\S+) - - \[(?P<time>.*?)\] "(?P<method>\S+) (?P<path>\S+) .*?" (?P<status>\d{3}) (?P<bytes>\S+)')

SAMPLE_LOGS = """
192.168.1.1 - - [04/Oct/2026:10:00:00] "GET /index.html HTTP/1.1" 200 4520
192.168.1.2 - - [04/Oct/2026:10:00:05] "POST /api/login HTTP/1.1" 200 120
192.168.1.1 - - [04/Oct/2026:10:00:10] "GET /dashboard HTTP/1.1" 302 0
10.0.0.5 - - [04/Oct/2026:10:00:15] "GET /secret HTTP/1.1" 403 240
192.168.1.1 - - [04/Oct/2026:10:00:20] "GET /images/logo.png HTTP/1.1" 200 8900
"""

def analyze_logs(log_data: str) -> dict:
    ip_counter = Counter()
    status_counter = Counter()
    for line in log_data.strip().splitlines():
        match = LOG_PATTERN.match(line)
        if match:
            data = match.groupdict()
            ip_counter[data["ip"]] += 1
            status_counter[data["status"]] += 1
    return {"top_ips": ip_counter.most_common(2), "statuses": dict(status_counter)}

if __name__ == "__main__":
    print("--- 077: Web Log Analyzer ---")
    results = analyze_logs(SAMPLE_LOGS)
    print("Top IPs:", results["top_ips"])
    print("Status codes breakdown:", results["statuses"])

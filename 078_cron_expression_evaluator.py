"""Program 078: Cron Expression Field Evaluator."""
def match_cron_field(field_spec: str, val: int) -> bool:
    if field_spec == "*":
        return True
    if "/" in field_spec:
        base, step = field_spec.split("/")
        return (val % int(step)) == 0
    if "," in field_spec:
        return val in [int(x) for x in field_spec.split(",")]
    if "-" in field_spec:
        start, end = field_spec.split("-")
        return int(start) <= val <= int(end)
    return int(field_spec) == val

def cron_matches(cron_expr: str, minute: int, hour: int, day: int, month: int, weekday: int) -> bool:
    parts = cron_expr.split()
    if len(parts) != 5:
        raise ValueError("Invalid cron syntax, requires 5 fields.")
    m_ok = match_cron_field(parts[0], minute)
    h_ok = match_cron_field(parts[1], hour)
    d_ok = match_cron_field(parts[2], day)
    mo_ok = match_cron_field(parts[3], month)
    w_ok = match_cron_field(parts[4], weekday)
    return m_ok and h_ok and d_ok and mo_ok and w_ok

if __name__ == "__main__":
    print("--- 078: Cron Expression Evaluator ---")
    expr = "*/15 9-17 * * 1-5" # Every 15 mins during 9-5 on weekdays
    matches = cron_matches(expr, minute=30, hour=14, day=4, month=10, weekday=2)
    print(f"Schedule '{expr}' matches 14:30 on Tuesday? {matches}")

"""Program 076: Gregorian Calendar Generator."""
def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year: int, month: int) -> int:
    month_days = [31, 29 if is_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 1]

def day_of_week(y: int, m: int, d: int) -> int:
    # Sakamoto's algorithm (0 = Sunday, 1 = Monday, ...)
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if m < 3:
        y -= 1
    return (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7

def print_month(year: int, month: int):
    header = f"{year} - Month {month}".center(20)
    print(header)
    print("Su Mo Tu We Th Fr Sa")
    start_day = day_of_week(year, month, 1)
    days = days_in_month(year, month)
    line = ["  "] * start_day
    for d in range(1, days + 1):
        line.append(f"{d:2d}")
        if len(line) == 7:
            print(" ".join(line))
            line = []
    if line:
        print(" ".join(line))

if __name__ == "__main__":
    print("--- 076: Calendar Month Generator ---")
    print_month(2026, 10)

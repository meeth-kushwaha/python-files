"""Program 036: CSV Parser and Formatter from Scratch."""
def parse_csv(csv_text: str, delimiter: str = ",") -> list[list[str]]:
    rows = []
    for line in csv_text.strip().splitlines():
        cells, curr, in_quotes = [], [], False
        i = 0
        while i < len(line):
            ch = line[i]
            if ch == '"':
                if in_quotes and i + 1 < len(line) and line[i + 1] == '"':
                    curr.append('"')
                    i += 1
                else:
                    in_quotes = not in_quotes
            elif ch == delimiter and not in_quotes:
                cells.append("".join(curr))
                curr = []
            else:
                curr.append(ch)
            i += 1
        cells.append("".join(curr))
        rows.append(cells)
    return rows

def to_csv(rows: list[list[str]], delimiter: str = ",") -> str:
    lines = []
    for row in rows:
        formatted = []
        for cell in row:
            if delimiter in cell or '"' in cell or "\n" in cell:
                escaped = cell.replace('"', '""')
                formatted.append(f'"{escaped}"')
            else:
                formatted.append(cell)
        lines.append(delimiter.join(formatted))
    return "\n".join(lines)

if __name__ == "__main__":
    print("--- 036: CSV Parser and Writer ---")
    data = [
        ["ID", "Name", "Note"],
        ["1", "Alice Smith", "Engineer, Lead"],
        ["2", 'Bob "The Builder"', "Contractor"]
    ]
    csv_str = to_csv(data)
    print("Generated CSV:\n" + csv_str)
    parsed = parse_csv(csv_str)
    print("\nRound-trip rows count:", len(parsed))

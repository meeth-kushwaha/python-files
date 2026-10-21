"""Program 049: Lightweight Markdown to HTML Converter."""
import re

def markdown_to_html(md: str) -> str:
    html_lines = []
    for line in md.splitlines():
        # Headers
        if line.startswith("### "):
            line = f"<h3>{line[4:]}</h3>"
        elif line.startswith("## "):
            line = f"<h2>{line[3:]}</h2>"
        elif line.startswith("# "):
            line = f"<h1>{line[2:]}</h1>"
        else:
            # Inline bold & italics
            line = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", line)
            line = re.sub(r"\*(.*?)\*", r"<em>\1</em>", line)
            # Inline code
            line = re.sub(r"`(.*?)`", r"<code>\1</code>", line)
            # Links [text](url)
            line = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', line)
            if line.strip():
                line = f"<p>{line}</p>"
        html_lines.append(line)
    return "\n".join(html_lines)

if __name__ == "__main__":
    print("--- 049: Mini Markdown to HTML ---")
    md_sample = "# Title\nThis is **bold** and *italic* with `code` and [Docs](https://python.org)."
    print(markdown_to_html(md_sample))

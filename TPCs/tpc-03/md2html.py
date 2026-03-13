import re
import sys
from collections import Counter


def convert_headings(line):
    match = re.match(r"^(#{1,6}) (.+)$", line)
    if match:
        level = len(match.group(1))
        content = match.group(2)
        return f"<h{level}>{content}</h{level}>"
    return line


def convert_inline(line):
    line = re.sub(
        r"(?<![a-zA-Z0-9])\*\*(?! )(.+?)(?<! )\*\*(?![a-zA-Z0-9])",
        r"<strong>\1</strong>",
        line,
    )
    line = re.sub(
        r"(?<![a-zA-Z0-9])\*(?! )(.+?)(?<! )\*(?![a-zA-Z0-9])", r"<em>\1</em>", line
    )
    return line


def convert_markdown(text):
    lines = text.splitlines()
    output = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # unordered list
        if re.match(r"^- .+", line):
            output.append("<ul>")
            while i < len(lines) and re.match(r"^- .+", lines[i]):
                item = re.sub(r"^- ", "", lines[i])
                item = convert_inline(item)
                output.append(f"  <li>{item}</li>")
                i += 1
            output.append("</ul>")
            continue

        # ordered list
        if re.match(r"^\d+\. .+", line):
            output.append("<ol>")
            while i < len(lines) and re.match(r"^\d+\. .+", lines[i]):
                item = re.sub(r"^\d+\. ", "", lines[i])
                item = convert_inline(item)
                output.append(f"  <li>{item}</li>")
                i += 1
            output.append("</ol>")
            continue

        # headings
        converted = convert_headings(line)
        if converted != line:
            output.append(convert_inline(converted))
        else:
            output.append(convert_inline(line))

        i += 1

    return "\n".join(output)


def count_tags(html):
    tags = re.findall(r"<([a-zA-Z][a-zA-Z0-9]*)[^>]*>", html)
    return Counter(tags)


def main():
    if len(sys.argv) < 2:
        print("Usage: python md2html.py <ficheiro.md>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Erro: ficheiro '{filename}' não encontrado.")
        sys.exit(1)

    html = convert_markdown(text)

    out_filename = re.sub(r"\.md$", ".html", filename)
    with open(out_filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Convertido: {filename} → {out_filename}")
    print()

    counts = count_tags(html)
    if counts:
        print("Contagem de tags geradas:")
        for tag, count in sorted(counts.items()):
            print(f"  <{tag}>: {count}")
    else:
        print("Nenhuma tag HTML gerada.")


if __name__ == "__main__":
    main()

with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

text = "".join(lines)

letters = sum(1 for c in text if c.isalpha())

words = len(text.split())

lines_count = len(lines)

print(f"Input file contains:")
print(f"{letters} letters")
print(f"{words} words")
print(f"{lines_count} lines")

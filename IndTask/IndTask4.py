import re

with open("input1.txt", "r", encoding="utf-8") as f:
    forbidden_words = f.read().split()

text = input("Введите предложение: ")

for word in forbidden_words:
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    text = pattern.sub("*" * len(word), text)

print("\nРезультат замены:")
print(text)

from collections import Counter

with open("file1.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

words = [word.strip(".,!?;:()[]«»\"'") for word in text.split()]
word_count = len(words)

most_common = Counter(words).most_common(1)[0]

print(f"Количество слов: {word_count}")
print(f"Самое частое слово: '{most_common[0]}' встречается {most_common[1]} раз(а)")


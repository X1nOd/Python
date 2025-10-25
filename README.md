# Тема 7. Работа с файлами (ввод, вывод)
Отчет по теме № 7 подготовил: Сидоров Вадим Викторович Пиэ-23-1

Лабораторные работы  
|Задание|Выполнил|                 
|-------|--------|
|   1   |    +   |
|   2   |    +   |
|   3   |    +   |
|   4   |    +   |
|   5   |    +   |
|   6   |    +   |
|   7   |    +   |
|   8   |    +   |
|   9   |    +   |
|  10   |    +   |
 Самостоятельные задания
 |Задание|Выполнил|
 |   1   |    +   |
 |   2   |    +   |
 |   3   |    +   |
 |   4   |    +   |
 |   5   |    +   |
 # Лабораторные работы
 # Задание 1
 <img width="304" height="331" alt="image" src="https://github.com/user-attachments/assets/92a12ef8-daf9-456e-a320-46a6325bc1c2" /> <br>
 # Задание 2
 <img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/2c50a1f4-ea25-4a86-ba11-186d2218af30" /> <br>
 # Задание 3
 <img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/b2d4b3cb-8d14-4369-b376-9c4f05946309" /> <br>
 # Задание 4
 <img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/648522cc-7e69-438e-a4ec-7a8a5c205ffa" /> <br>
 # Задание 5
 <img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/3c19ec55-95da-4fc0-8517-ffd58b0e855f" /> <br>
 # Задание 6
 <img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/20b6418a-0ad2-4dd6-acea-e583d891b6ab" /> <br>
 <img width="791" height="556" alt="image" src="https://github.com/user-attachments/assets/c47442f8-f993-447d-ac1d-147ceb0723ba" /> <br>
# Задание 7
<img width="1013" height="1023" alt="image" src="https://github.com/user-attachments/assets/ce588ea8-37cd-4b8f-af5c-c1e5046150dc" /> <br>
<img width="800" height="557" alt="image" src="https://github.com/user-attachments/assets/a287f4bc-3009-49b6-ba4a-3b2cbe7defe3" /> <br>
# Задание 8
<img width="832" height="1080" alt="image" src="https://github.com/user-attachments/assets/900a133c-263e-444f-8916-b42de5ce1906" /> <br>
# Задание 9
<img width="805" height="1080" alt="image" src="https://github.com/user-attachments/assets/c5a6dcfa-e5cc-4886-966d-27515ae85a87" /> <br>
# Задание 10
<img width="803" height="1080" alt="image" src="https://github.com/user-attachments/assets/fafb862d-1cc8-4b9c-b496-1282314b523e" /> <br>
# Лабораторные работы
# Задание 1
<pre> from collections import Counter

with open("file1.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

words = [word.strip(".,!?;:()[]«»\"'") for word in text.split()]
word_count = len(words)

most_common = Counter(words).most_common(1)[0]

print(f"Количество слов: {word_count}")
print(f"Самое частое слово: '{most_common[0]}' встречается {most_common[1]} раз(а)") </pre>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ace803f4-dd8c-4662-9826-27bb6809510c" /> <br>
# Задание 2
<pre>def load_expenses(filename="expenses.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_expenses(expenses, filename="expenses.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for e in expenses:
            f.write(e + "\n")

def main():
    expenses = load_expenses()
    while True:
        print("\n1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            item = input("Введите описание расхода: ")
            amount = input("Введите сумму: ")
            record = f"{item} - {amount} руб."
            expenses.append(record)
            save_expenses(expenses)
            print("Расход добавлен!")
        elif choice == "2":
            if expenses:
                print("\nСписок расходов:")
                for e in expenses:
                    print(e)
            else:
                print("Список пуст.")
        elif choice == "3":
            break
        else:
            print("Неверный ввод!")

if __name__ == "__main__":
    main()</pre>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ad5890d4-2194-4d84-9341-1e9258eeb48e" /> <br>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/562a59bb-360c-4d6b-bb13-92bf0e75a846" /> <br>
# Задание 3
<pre>with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

text = "".join(lines)

letters = sum(1 for c in text if c.isalpha())

words = len(text.split())

lines_count = len(lines)

print(f"Input file contains:")
print(f"{letters} letters")
print(f"{words} words")
print(f"{lines_count} lines")</pre>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/878812f5-edb6-492d-8a31-83e791e10037" /> <br>
# Задание 4
<pre>import re

with open("input1.txt", "r", encoding="utf-8") as f:
    forbidden_words = f.read().split()

text = input("Введите предложение: ")

for word in forbidden_words:
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    text = pattern.sub("*" * len(word), text)

print("\nРезультат замены:")
print(text)
</pre>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/50cc01bc-f61a-4c18-91cb-45fa7c7c2702" /> <br>
# Задание 5
<pre>def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Удалить задачу")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            task = input("Введите задачу: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Задача добавлена!")
        elif choice == "2":
            if tasks:
                print("\nСписок задач:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
            else:
                print("Список задач пуст.")
        elif choice == "3":
            if tasks:
                num = int(input("Введите номер задачи для удаления: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"Удалена задача: {removed}")
                else:
                    print("Неверный номер.")
            else:
                print("Список пуст.")
        elif choice == "4":
            break
        else:
            print("Неверный ввод!")

if __name__ == "__main__":
    main()</pre>
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/daf48de3-56c1-43c6-b782-bfdc6f394921" />



















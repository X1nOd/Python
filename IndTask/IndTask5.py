def load_tasks(filename="tasks.txt"):
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
    main()

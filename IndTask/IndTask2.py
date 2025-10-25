def load_expenses(filename="expenses.txt"):
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
    main()

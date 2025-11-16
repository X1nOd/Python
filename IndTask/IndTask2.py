def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().strip()
            if not data:
                raise ValueError("Файл пустой!")
            return data
    except FileNotFoundError:
        return "Файл не найден"
    except ValueError as e:
        return str(e)


print(read_file("empty.txt"))


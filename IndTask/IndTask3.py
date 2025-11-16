def sum_two(n):
    try:
        if not isinstance(n, (int, float)):
            raise TypeError("Неподходящий тип данных. Ожидалось число.")
        return n + 2
    except TypeError as e:
        return str(e)


try:
    user_value = input("Введите число: ")
    if "." in user_value:
        user_value = float(user_value)
    else:
        user_value = int(user_value)
except ValueError:
    user_value = user_value


print(sum_two(user_value))
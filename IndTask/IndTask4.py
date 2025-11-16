def custom_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} выполнена")
        return result
    return wrapper


@custom_decorator
def greet(name):
    print(f"Привет, {name}!")


@custom_decorator
def add(a, b):
    return a + b
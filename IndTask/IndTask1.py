import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\nВремя выполнения: {end - start} секунд")
        return result
    return wrapper


@time_decorator
def fibonacci():
    f1 = f2 = 1
    for _ in range(2, 200):
        f1, f2 = f2, f1 + f2
        print(f2, end=' ')


if __name__ == '__main__':
    fibonacci()
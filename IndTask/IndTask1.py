def fibonacci(n):
    a, b = 1, 1
    for num in range(n):
        yield a
        a, b = b, a + b

n = 252
fibonacci_numbers = list(fibonacci(n))


print(fibonacci_numbers[-1])

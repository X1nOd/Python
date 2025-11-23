def fibonacci(n):
    a, b = 1, 1
    with open('fibonacci.txt', 'w') as f:
        for _ in range(n):
            f.write(f"{a}\n")
            yield a
            a, b = b, a + b

n = 243
fibonacci_numbers = list(fibonacci(n))

print(fibonacci_numbers[-1])
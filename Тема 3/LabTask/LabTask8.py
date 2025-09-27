value = 0
while value < 1000:
    if value == 0:
        value += 100
    elif value % 2 == 0:
        value //= 2
    elif value > 500:
        value *= 2
    else:
        value *= 7
    print(value)

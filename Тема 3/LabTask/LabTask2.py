number = int(input('Введите число: '))
if number < 0:
    print('Число меньше 0.')
elif 0 < number < 10:
    print('Число больше 0, но меньше 10.')
else:
    print('Число больше 10.')
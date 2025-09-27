number = int(input('Введите число от 1 до 10 '))
if number > 10:
    print('Число больше 10.')
elif 0 < number <= 3:
    print('Число больше 0, но меньше 3')
elif 3 < number <= 6:
    print('Число больше 3, но меньше 6')
else:
    print('Число больше 6, но меньше 10')

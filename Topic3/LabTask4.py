numbers = [25, 4, 67, 92, 1]
value = int(input('Введите число: '))
if value in numbers:
    if value % 2 == 0:
        print('Число есть в массиве и оно чётное')
    else:
        print('Число есть в массиве и оно нечётное')
else:
    print('Числа нет в массиве')
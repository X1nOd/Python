array = [2, 3, 5, 10, 99]
flag = False
for value in array:
    if value % 2 == 1:
        flag = True
if flag is True:
    print('В массиве есть нечётное число')
else:
    print('Все чётные')
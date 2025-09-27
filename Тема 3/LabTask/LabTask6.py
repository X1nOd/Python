string = 'Привет всем изучающим Python!'
value = input('Введите букву: ')
for i in string:
    if i == value:
        index = string.find(value)
        print("Буква "+ value +" есть в строке под "+ str(index) + " индексом.")
        break
else:
    print('Буквы ' + value + ' нет в этой строке')
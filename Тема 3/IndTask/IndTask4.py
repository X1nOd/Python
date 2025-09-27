for i in range(3):
    sentence = input("Введите предложение на английском: ")

    print("Длина предложения:", len(sentence))

    lower_sentence = sentence.lower()
    print("Предложение в нижнем регистре:", lower_sentence)

    vowels = "aeiou"
    count = 0
    for ch in lower_sentence:
        if ch in vowels:
            count = count + 1
    print("Количество гласных:", count)

    replaced = lower_sentence.replace("ugly", "beauty")
    print("После замены:", replaced)

    if lower_sentence.startswith("the"):
        print("Предложение начинается с 'The'")
    else:
        print("Предложение не начинается с 'The'")

    if lower_sentence.endswith("end"):
        print("Предложение заканчивается на 'end'")
    else:
        print("Предложение не заканчивается на 'end'")

    print("-----------------------------")

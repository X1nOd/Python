one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
def new(learing):
    result = []
    for grade in learing:
        if grade == 2:
            continue
        if grade == 3:
            result.append(4)
        else:
            result.append(grade)
    return result
print(new(one))
print(new(two))
print(new(three))
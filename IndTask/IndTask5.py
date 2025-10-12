def list_to_set(lst):
    result = set()
    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1
    for num, count in count.items():
        result.add(num)
        for i in range(2, count + 1):
            result.add(str(num) * i)
    return result

list1 = [1, 1, 3, 3, 1]
list2 = [5, 5, 5, 5, 5, 5, 5]
list3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(list_to_set(list1))
print(list_to_set(list2))
print(list_to_set(list3))
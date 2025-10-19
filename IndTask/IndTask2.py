def remove_first_occurrence(t, elem):
    if elem not in t:
        return t
    lst = list(t)
    
    lst.remove(elem)
    
    return tuple(lst)

print(remove_first_occurrence((1, 2, 3), 1))
print(remove_first_occurrence((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2, 3), 3))
print(remove_first_occurrence((2, 4, 6, 6, 4, 2, 9), 9))
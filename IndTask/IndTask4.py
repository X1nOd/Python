def slice_tuple_by_element(t, elem):
    if elem not in t:
        return ()

    first = t.index(elem)

    try:
        second = t.index(elem, first + 1)
        return t[first:second + 1]
    except ValueError:
        return t[first:]

print(slice_tuple_by_element((1, 2, 3), 8))
print(slice_tuple_by_element((1, 8, 3, 4, 8, 4, 8, 9, 2), 8))
print(slice_tuple_by_element((1, 2, 8, 5, 1, 2, 9), 8))

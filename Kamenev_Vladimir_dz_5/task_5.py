src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def unduble_set(list_number):
    _set = set()
    for el in list_number:
        if el in _set:
            _set.remove(el)
        else:
            _set.add((el))
    return _set


src_set = unduble_set(src)
result = [el for el in src if el in src_set]
print(result)

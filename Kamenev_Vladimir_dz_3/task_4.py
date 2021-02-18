

def add_item(dic, key1, key2, add_it):
    """Добавление элементов во вложенный список словаря по ключам"""
    dic[key1][key2].append(add_it)
    return dic


def thesaurus_adv(*nams_surnames):
    list_workers = {}
    for i in nams_surnames:
        _nams_surnames = i.split(' ')
        if _nams_surnames[1][0] in list_workers:
            _temp = list_workers[_nams_surnames[1][0]]
            if _nams_surnames[1][0] in _temp:
                add_item(list_workers, _nams_surnames[1][0], _nams_surnames[0][0], i)
            else:
                list_workers[_nams_surnames[1][0]].setdefault(_nams_surnames[0][0], [])
                add_item(list_workers, _nams_surnames[1][0], _nams_surnames[0][0], i)
        else:
            list_workers.setdefault(_nams_surnames[1][0], {})
            list_workers[_nams_surnames[1][0]].setdefault(_nams_surnames[0][0], [])
            add_item(list_workers, _nams_surnames[1][0], _nams_surnames[0][0], i)
    return list_workers


dictionary_workers = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
                                   "Анна Савельева", "Ибрагим Измаилов", "Иван Сидоров")
print((dictionary_workers))

# выводим отсортированный словарь по ключам первого уровня
print('Вывод значений словоря по отсортированным ключам')
for key in sorted(dictionary_workers):
    print(f'{key}: {dictionary_workers[key]}')

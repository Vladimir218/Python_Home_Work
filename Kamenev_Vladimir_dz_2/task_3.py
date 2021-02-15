positions = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
# вариант с созданием списка
print("Вывод имен с созданием списка")
for i in positions:
    _name = i.split(' ')[-1].capitalize()
    print(f'Привет, {_name}!')
    _name = ""
print("Вывод имен без создания списка")
for ind, _str in enumerate(positions):
    _str.title()
    _log = 0
    ind1 = 0
    while _log == 0:
        ind1 = _str.find(" ", ind1)
        if ind1 > 0:
            ind1 += 1
            _ind = ind1
        else:
            _log = 1
    _name = _str[_ind:].title()
    print(f'Привет, {_name}!')

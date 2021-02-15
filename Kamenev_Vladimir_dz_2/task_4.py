price = [57.89, 54.3, 78.6, 27.89, 97, 89, 56.78, 89.01, 98.74, 82, 67]
print("Пункт A")
massage = ""
for i in price:
    _price = str(i).split('.')
    if len(_price) == 1:
        massage += f'{_price[0]} руб 00 коп, '
    else:

        cent = _price[1]
        if len(cent) == 1:
            if int(cent) < 10:
                cent = int(cent) * 10
        massage += f'{_price[0]} руб {cent} коп, '
massage = massage[:-2]
print(massage)
print("Пункт B")
print("Адрес списка цен - ", id(price))
price.sort()
print("Адрес списка цен после сортировки - ", id(price))
print(price)
print("Пункт C")
new_price = price[::-1]
print("Адрес нового списка цен - ", id(new_price))
print("Адрес исходного списка цен - ", id(price))
print('Новый пересортированный список :\n', new_price)
print("Пункт D")
print(f'Стоимость пяти самых дорогих товаров: {price[-5:]}')

a = float(input('Введите делимое '))
b = float(input('Введите делитель '))

try:
    rez = a / b
    print(f'Результат деления - {rez}')
except ZeroDivisionError:
    print('Результат деления - бесконечность')

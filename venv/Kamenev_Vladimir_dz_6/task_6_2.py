from sys import argv

"""Чтение данных из файла bakery.csv по правилу:
- запуск скрипта выводит все записи
- запуск скрипта с однним дополнитеьным параметром - выводит данные с указанной строки до конца файла
- запуск скрипта с дву мя параметрами - выводит данные начиная с указанной записи (первое число)
 до записи включительно(второе число) """


def show_data(save_file_name, start=0, finish=0):
    with open(save_file_name, 'r', encoding='UTF-8') as f:
        if start == 0 and finish == 0:
            for line in f:
                print(line, end='')
        elif start > 0 and finish == 0:
            i = 1
            for line in f:
                if i >= start:
                    print(line, end='')
                i += 1
        elif start > 0 and finish >= start:
            i = 1
            for line in f:
                if finish >= i >= start:
                    print(line, end='')
                i += 1
    return


param = argv[1:]
file_name = "bakery.csv"
if len(param) == 0:
    show_data(file_name)
elif len(param) == 1:
    show_data(file_name, int(param[0]))
elif len(param) == 2:
    show_data(file_name, int(param[0]), int(param[1]))
else:
    print('Введены некорректные данные')

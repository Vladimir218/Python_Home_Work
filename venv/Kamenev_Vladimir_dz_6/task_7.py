from sys import argv

"""Перезапись данных файла bakery.csv в определенной строке по правилу:
первый параметр - номер строки
второй параметр - новое значение
"""


def edit_data(save_file_name, str_num, data):
    start = 0
    log = 0
    if str_num > 1:
        with open(save_file_name, 'r', encoding='UTF-8') as f:
            i = 1
            line = 1
            while line:
                start = f.tell()
                line = f.readline()
                if i == str_num:
                    log = 1
                    long = len(line.strip())
                    break
                i += 1
    if log == 1 or start == 0:
        with open(save_file_name, 'r+', encoding='UTF-8') as f:
            f.seek(start)
            print(f.tell())
            f.write(data)
            long1 = len(str(data))
            if long > long1:
                f.write(' ' * (long - long1))
    else:
        print('Введены некорректные данные')
    return


param = argv[1:]
file_name = "bakery.csv"
if len(param) != 2:
    print('Введены некорректные данные')
else:
    edit_data(file_name, int(param[0]), param[1])

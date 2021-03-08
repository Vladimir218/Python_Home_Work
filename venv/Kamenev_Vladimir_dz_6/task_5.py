from sys import argv
from json import dump, load
from itertools import zip_longest

"""Объединение данных из файлов с данными пользователей и их хобби из командной строки. Результат сохраняется в новый файл.
 формат: task_5.py user hobbi out
 user - путь и имя файла с данными пользователей
 hobbi - путь и имя файла с хобби пользователя
 out - путь и имя фыходного файла
При реализации алгоритма предполагается, что количество участников и их хобби одинаковое, 
если данные в файлах не совпадают, то программа остановится, как закончатся жданные в одном из файлов"""
user, hobbi, out_file = argv[1:4]
with open(user, 'r', encoding='UTF-8') as names:
    with open(hobbi, 'r', encoding='UTF-8') as hobbis:
        name_gen = (" ".join(lines.replace('\ufeff', '').strip().split(',')) for lines in names)
        hobbi_gen = (lines.replace('\ufeff', '').strip() for lines in hobbis)
        hf = open(out_file, 'w', encoding='UTF-8')
        try:
            while True:
                hf.write(f'{next(name_gen)}: {next(hobbi_gen)}\n')
        except:
            hf.close()

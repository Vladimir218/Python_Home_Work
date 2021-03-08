from json import dump, load
from itertools import zip_longest

"""При реализации алгоритма предполагается, что количество участников и их хобби одинаковое, 
если данные в файлах не совпадают, то программа остановится, как закончатся жданные в одном из файлов"""
with open('name.csv', 'r', encoding='UTF-8') as names:
    with open('hobbi.csv', 'r', encoding='UTF-8') as hobbis:
        name_gen = (" ".join(lines.replace('\ufeff', '').strip().split(',')) for lines in names)
        hobbi_gen = (lines.replace('\ufeff', '').strip() for lines in hobbis)
        hf = open('hobbi_file.txt', 'w', encoding='UTF-8')
        try:
            while True:
                hf.write(f'{next(name_gen)}: {next(hobbi_gen)}\n')
        except:
            hf.close()

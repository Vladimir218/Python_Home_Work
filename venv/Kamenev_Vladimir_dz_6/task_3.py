from json import dump, load
from itertools import zip_longest

with open('name.csv', 'r', encoding='UTF-8') as names:
    with open('hobbi1.csv', 'r', encoding='UTF-8') as hobbis:
        hobbi_list = zip_longest((" ".join(lines.replace('\ufeff', '').strip().split(',')) for lines in names),
                                 ((lines.replace('\ufeff', '').strip()) for lines in hobbis), fillvalue=None)
        hobbi_dic = {name: hobbi for name, hobbi in hobbi_list}
        if None in hobbi_dic.keys():
            print(1)
        else:
            with open('hobbi_file.json', 'w', encoding='UTF-8') as hf:
                dump(hobbi_dic, hf, ensure_ascii=False, indent=4)
with open('hobbi_file.json', 'r', encoding="UTF-8") as hf:
    print(load(hf))

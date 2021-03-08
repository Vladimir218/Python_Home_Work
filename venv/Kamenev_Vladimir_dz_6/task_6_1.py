from sys import argv

"""Внесение в файл bakery.csv  данных о продажах"""


def save_mony(mony_list, save_file_name):
    with open(save_file_name, 'a', encoding='UTF-8') as f:
        for mony in mony_list:
            f.write(mony + '\n')
    return


mony = argv[1:]
file_name = "bakery.csv"
if len(mony) > 0:
    save_mony(mony, file_name)

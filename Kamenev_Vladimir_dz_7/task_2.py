"""Создает структуру проекта из папок и файлов заданную в config.yaml
при формировании config.yaml должны выполняться правила:
- проект начинается родительской папкой
- структура вложения:
    - вначале указывается родительская папка
    - далее вложенные в нее файлы
    - далее вложенные подпапки.
- вложение должно задаваться сдвигом на 3 пробела относительно родительской папки.
дополнительные вложения папок и файлов должно удовлетворять выше описанному правилу

файл с описанной структурой приложен config.yaml"""

import os


def get_path(old_key, new_key, path_dir, new_item):
    if new_key < old_key:
        for i in range(int((old_key - new_key) / 3 + 1)):
            path_dir.pop()
    elif new_key == old_key:
        if len(path_dir) > 0:
            path_dir.pop()
    path_dir.append(new_item.strip())
    return [new_key, path_dir]


with open('config.yaml', 'r', encoding='UTF-8') as f:
    path_project = []
    key = 0
    for line in f:
        *path_key, item = line.split(' ')
        if '.' in item:
            if not os.path.exists(os.path.join(*path_project, item.strip())):
                with open(os.path.join(*path_project, item.strip()), 'w', encoding='UTF-8') as new_file:
                    new_file.write('')
        else:
            key, path_project = get_path(key, len(path_key), path_project, item)
            if not os.path.exists(os.path.join(*path_project)):
                os.makedirs(os.path.join(*path_project))

"""Процедурва для создания структуры папок по заданному в словаре шаблону.
Шаблон может изменяться и содержать различное количество вложенных папок"""
import os

project_structure = {'my_project':
                         {'settings':
                              {},
                          'mainapp':
                              {},
                          'adminapp':
                              {},
                          'authapp':
                              {}
                          }
                     }


def generate_project_structure(start_path, dir_dictionary={}):
    if len(dir_dictionary) > 0:
        for key, dictionary in dir_dictionary.items():
            generate_project_structure(f'{start_path}/{key}', dictionary)
    else:
        if not os.path.exists(f'{start_path[1:]}'):
            try:
                os.makedirs(f'{start_path[1:]}')
            except FileNotFoundError:
                return
    return


if __name__ == '__main__':
    generate_project_structure("", project_structure)

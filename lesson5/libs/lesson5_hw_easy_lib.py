# библиотека функций для задания normal

import os
import shutil


def print_menu():
    print('\nМеню операций:')
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')


def my_cd(path):
    try:
        os.chdir(path)
        print(f'Текущая директория: {path}')
    except FileNotFoundError:
        print(f'Директория не найдена!')
    except PermissionError:
        print('Невозможно перейти!')


def my_ls():
    try:
        list_cur_dir = os.listdir(os.path.join(os.getcwd()))
        print('Содержимое текущей директории: ')
        for i in range(len(list_cur_dir)):
            print(list_cur_dir[i])
    except PermissionError:
        print('Невозможно отобразить содержимое!')


def my_rm(dir_name):
    try:
        shutil.rmtree(dir_name)
        print(f'Директория {dir_name} удалена')
    except FileNotFoundError:
        print(f'Директория {dir_name} не найдена')
    except PermissionError:
        print('Невозможно удалить!')


def my_mkdir(dir_name):
    try:
        os.mkdir(os.path.join(os.getcwd(), dir_name))
        print(f'Директория {dir_name} создана')
    except FileExistsError:
        print(f'Директория {dir_name} уже существует')
    except PermissionError:
        print('Невозможно создать!')

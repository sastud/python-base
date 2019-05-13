# библиотека функций для задания hard

import os
import shutil


def print_help():
    print('\n')
    print('help - получение справки')
    print('mkdir <dir_name> - создание директории')
    print('ping - тестовый ключ')
    print('cp <file_name> - создание копии указанного файла')
    print('rm <file_name> - удаление указанного файла')
    print('cd <full_path or relative_path> - смена текущей директории на указанную')
    print('pwd - отображение полного пути текущей директории')
    print('ls - отображение содержимого текущей директории')


def make_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
    except PermissionError:
        print('Невозможно создать директорию!')


def ping():
    print("pong")


def my_cp(file_name):
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        shutil.copy2(os.path.abspath(file_name), os.path.abspath(file_name) + '.copy')
        print(f'Файл {file_name}.copy создан/перезаписан')
    except FileNotFoundError:
        print(f'Файл {file_name} не найден')
    except PermissionError:
        print('Невозможно создать копию файла!')


def my_rm(file_name):
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    cn = input(f'Подтверждаете удаление файла {file_name}, y/n?: ')
    if cn == 'y':
        try:
            os.remove(os.path.abspath(file_name))
            print(f'Файл {file_name} удален')
        except FileNotFoundError:
            print(f'Файл {file_name} не найден')
        except PermissionError:
            print('Невозможно удалить файл!')
    elif cn == 'n':
        print('Отменено')
    else:
        print('Некорректный ввод!')


def my_cd(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.chdir(dir_name)
        print(f'Текущая директория: {dir_name}')
    except FileNotFoundError:
        print(f'Директория не найдена!')
    except PermissionError:
        print('Невозможно перейти!')


def my_pwd():
    print('Полный путь текущей директории:\n', os.getcwd())


def my_ls():
    try:
        list_cur_dir = os.listdir(os.path.join(os.getcwd()))
        print('Содержимое текущей директории: ')
        for i in range(len(list_cur_dir)):
            print(list_cur_dir[i])
    except PermissionError:
        print('Невозможно отобразить содержимое!')

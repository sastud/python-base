# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys
import shutil
# print('sys.argv = ', sys.argv)


def print_help():
    print('help - получение справки')
    print('mkdir <dir_name> - создание директории')
    print('ping - тестовый ключ')
    print('cp <file_name> - создание копии указанного файла')
    print('rm <file_name> - удаление указанного файла')
    print('cd <full_path or relative_path> - смена текущей директории на указанную')
    print('pwd - отображение полного пути текущей директории')


def make_dir():
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


def my_cp():
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


def my_rm():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        os.remove(os.path.abspath(file_name))
        print(f'Файл {file_name} удален')
    except FileNotFoundError:
        print(f'Файл {file_name} не найден')
    except PermissionError:
        print('Невозможно удалить файл!')


def my_cd():
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


do = {
    'help': print_help,
    'mkdir': make_dir,
    'ping': ping,
    'cp': my_cp,
    'rm': my_rm,
    'cd': my_cd,
    'pwd': my_pwd
}

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

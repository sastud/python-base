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

import sys
import libs.lesson5_hw_hard_lib as hard_lib


do = {
    'help': hard_lib.print_help,
    'mkdir': hard_lib.make_dir,
    'ping': hard_lib.ping,
    'cp': hard_lib.my_cp,
    'rm': hard_lib.my_rm,
    'cd': hard_lib.my_cd,
    'pwd': hard_lib.my_pwd,
    'ls': hard_lib.my_ls
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

ch = input('\nПродолжить работу программы (y/n)?:\t')
if ch == 'y':
    while ch != 'exit':
        if ch == 'y':
            hard_lib.print_help()
            print('\nexit. Выход из программы')
        ch = input('\nВаш выбор: ')
        if ch == 'exit':
            print('\nЗавершение работы программы')
        elif ch == 'help':
            hard_lib.print_help()
        elif ch == 'mkdir':
            dir_name = input('\nУкажите создаваемую директорию: ')
            hard_lib.make_dir(dir_name)
        elif ch == 'ping':
            hard_lib.ping()
        elif ch == 'cp':
            file_name = input('\nУкажите копируемый файл: ')
            hard_lib.my_cp(file_name)
        elif ch == 'rm':
            file_name = input('\nУкажите удаляемый файл: ')
            hard_lib.my_rm(file_name)
        elif ch == 'cd':
            dir_name = input('\nУкажите директорию: ')
            hard_lib.my_cd(dir_name)
        elif ch == 'pwd':
            hard_lib.my_pwd()
        elif ch == 'ls':
            hard_lib.my_ls()
        else:
            print('Некорректный ввод!\n')
            hard_lib.print_help()
    print('\n')
elif ch == 'n':
    print('\nЗавершение работы программы')
else:
    print('Некорректный ввод!\n')
    hard_lib.print_help()

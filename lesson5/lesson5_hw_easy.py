# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

print('\nЗадача-1\n')

for i in range(1, 10):
    try:
        os.mkdir(os.path.join(os.getcwd(), f'dir_{i}'))
        print(f'Директория dir_{i} создана')
    except FileExistsError:
        print(f'Директория dir_{i} уже существует')

print(input('\nДалее созданные директории будут удалены. Нажмите ENTER для продолжения...'))

for i in range(1, 10):
    try:
        os.rmdir(os.path.join(os.getcwd(), f'dir_{i}'))
        print(f'Директория dir_{i} удалена')
    except FileNotFoundError:
        print(f'Директория dir_{i} не найдена')

###############################################################

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print('\n')
print('Задача-2\n')

print('Содержимое текущей директории: ')
list_cur_dir = os.listdir(os.path.join(os.getcwd()))
for i in range(len(list_cur_dir)):
    print(list_cur_dir[i])

###############################################################

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('\n')
print('Задача-3\n')

shutil.copy2(os.path.abspath(__file__), os.path.abspath(__file__) + '.copy.py')
print(f'Файл {__file__}.copy создан/перезаписан')

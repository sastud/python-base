
import os


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


print('Содержимое текущей директории: ')
list_cur_dir = os.listdir(os.path.join(os.getcwd()))
for i in range(len(list_cur_dir)):
    print(list_cur_dir[i])

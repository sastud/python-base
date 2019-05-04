
import os


def my_cd(path):
    os.chdir(path)
    print(f'Текущая директория: {path}')


def my_ls():
    print('Содержимое текущей директории: ')
    list_cur_dir = os.listdir(os.path.join(os.getcwd()))
    for i in range(len(list_cur_dir)):
        print(list_cur_dir[i])


def my_rm(dir_name):
    try:
        os.rmdir(os.path.join(os.getcwd(), dir_name))
        print(f'Директория {dir_name} удалена')
    except FileNotFoundError:
        print(f'Директория {dir_name} не найдена')


def my_mkdir(dir_name):
    try:
        os.mkdir(os.path.join(os.getcwd(), dir_name))
        print(f'Директория {dir_name} создана')
    except FileExistsError:
        print(f'Директория {dir_name} уже существует')

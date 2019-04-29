# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


print('\nЗадача-1\n')


def gcd_count(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    gcd = a + b
    return gcd


def result(str_in):
    list_in = list(str_in)

    for i in range(0, len(list_in) - 1):
        if list_in[i] == '-' and list_in[i - 2] == '-':
            list_in.pop(i)
            list_in[i - 2] = '+'

    for i in range(0, len(list_in) - 1):
        if list_in[i - 2] == '-':
            list_in[i - 2] = '+'
            list_in[i] = int(list_in[i]) * (-1)
            list_in[i] = str(list_in[i])

    for i in range(1, len(list_in) - 1):
        if list_in[i].isdigit() is True and list_in[i - 1].isdigit() is True:
            list_in[i] = list_in[i - 1] + list_in[i]
            list_in[i - 1] = ' '

    for i in range(4, len(list_in)):
        if list_in[i] == '+' and list_in[i - 1] == ' ' and list_in[i - 3] == ' ' and list_in[i - 4] == '+':
            list_in[i - 1:i - 1] = [' ', '0', '/', '1']

    if list_in[0].isdigit() is True and list_in[1] == ' ' and list_in[2] == '+':
        list_in[1:1] = [' ', '0', '/', '1']

    if list_in[len(list_in) - 1].isdigit() is True and list_in[len(list_in) - 2] == ' ':
        list_in[len(list_in):] = [' ', '0', '/', '1']

    while ' ' in list_in:
        list_in.remove(' ')
    while '+' in list_in:
        list_in.remove('+')

    for i in range(3, len(list_in)):
        if list_in[i - 1] == '/':
            if int(list_in[i - 3]) < 0:
                list_in[i - 2] = int(list_in[i]) * int(list_in[i - 3]) - int(list_in[i - 2])
            else:
                list_in[i - 2] = int(list_in[i]) * int(list_in[i - 3]) + int(list_in[i - 2])
            list_in[i - 3] = '^'

    while '^' in list_in:
        list_in.remove('^')

    list_del = []
    for i in range(0, len(list_in)):
        if list_in[i - 1] == '/':
            list_del.append(list_in[i])

    for i in range(0, len(list_del)):
        list_del[i] = int(list_del[i])

    from functools import reduce
    int_del = reduce((lambda x, y: x * y), list_del)

    for i in range(0, len(list_in)):
        if list_in[i - 1] == '/':
            list_in[i - 2] = list_in[i - 2] * (int_del / int(list_in[i]))
            list_in[i] = int_del

    list_ch = []
    for i in range(2, len(list_in)):
        if list_in[i - 1] == '/':
            list_ch.append(list_in[i - 2])

    for i in range(0, len(list_ch)):
        list_ch[i] = int(list_ch[i])

    int_ch = sum(list_ch)
    f_part = int_ch // int_del
    d_part = abs(int_ch) % int_del
    gcd = gcd_count(d_part, int_del)
    d_part_fin = int(d_part / gcd)
    int_del_fin = int(int_del / gcd)
    list_fin = [str(f_part), ' ', str(d_part_fin), '/', str(int_del_fin)]
    out = ''.join(list_fin)

    return out


string_in = '1 5/6 + 9 4/5 - 2 3/13 - -4 - 5 2/3 + 3'
# string_in = input('Введите выражение: ')
print('Введенная строка: ', string_in)
res = result(string_in)
print('Результат: ', res)

# Доделать случай отсутствия целой части дроби.
# А лучше сменить подход к решению...


###############################################################


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# ! Нужен пример вводных данных. Иначе непонятно, что считать...

###############################################################


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os


print('\n')
print('Задача-4\n')


def r_file(dir, f_name):
    path = os.path.join(dir, f_name)
    with open(path, 'r', encoding='UTF-8') as f:
        for l in f:
            l = l.capitalize()
            w_file('data', l)


def w_file(dir, line):
    path = os.path.join(dir, 'fruits_' + str(line[0]) + '.txt')
    with open(path, 'a', encoding='UTF-8') as f:
        f.write(line)


r_file('data', 'fruits.txt')


# Доделать проверку корректности наименований.

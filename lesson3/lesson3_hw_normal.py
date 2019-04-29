# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print('\nЗадача-1')


def fibonacci(n, m):
    fl = []
    for x in range(n, m + 1):
        fl.append(int((((1 + 5 ** 0.5) / 2) ** x - ((1 - 5 ** 0.5) / 2) ** x) / (5 ** 0.5)))
    return fl


n = int(input('Введите начальный элемент: '))
m = int(input('Введите конечный элемент: '))

res = fibonacci(n, m)
print('\nЗапрошенные элементы ряда: ', res)

###############################################################

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print('\n')
print('Задача-2\n')


def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        for j in range(1, len(origin_list)):
            if origin_list[j] < origin_list[j - 1]:
                k = origin_list[j - 1]
                origin_list[j - 1] = origin_list[j]
                origin_list[j] = k
    return origin_list


list_orig = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print('List sorted: ', sort_to_max(list_orig))

###############################################################

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print('\n')
print('Задача-3\n')


def my_filter(fun, arg):
    out = []
    for i in arg:
        if bool(fun(i)) is True:
            out.append(i)
    return out


in_list1 = [2, 10, -10, 8, 2, 0, 14]
in_list2 = ['', 'not null', 'bla', '', '10']
print(my_filter((lambda x: x > 5), in_list1))
print(my_filter(len, in_list2))

###############################################################

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print('\n')
print('Задача-4\n')


# вычисление длин отрезков
def length(p1, p2):
    l = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
    return l


# проверка признака параллелограмма
def par_check(l_list):
    if l_list[0] == l_list[2] and l_list[1] == l_list[3]:
        return 1
    else:
        return 0


A = [[0, 0], [2, 6], [8, 6], [6, 0]]
L = [length(A[0], A[1]), length(A[1], A[2]), length(A[2], A[3]), length(A[3], A[0])]

stat = par_check(L)

if stat == 1:
    print(A, '\nЭто параллелограмм')
else:
    print(A, '\nЭто иная фигура')

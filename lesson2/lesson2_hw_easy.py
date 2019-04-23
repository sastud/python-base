# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print('\nЗадача-1')
fruits = ['яблоко', 'банан', 'киви', 'арбуз']
print(fruits, '\n')
field = len(max(fruits))
for i, fruit in enumerate(fruits, 1):
    print(f'{i}. {fruit:>{field}}')

###############################################################

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print('\n')
print('Задача-2\n')
list1 = ['a', 'b', 'c', 'd', 'e', 'u', 'u']
list2 = ['a', 'c', 'e', 'k', 'w']
print([i for i in list1 if i not in list2])

###############################################################

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print('\n')
print('Задача-3\n')
list3 = [1, 2, 3, 4, 5, 6]
list4 = []

for i in list3:
    if i%2 == 0:
        list4.append(i/4)
    else:
        list4.append(i*2)

print(list4)
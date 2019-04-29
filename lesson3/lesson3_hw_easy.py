# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print('\nЗадача-1')


def my_round(number, ndigits):
    if (number * (10**ndigits)) % 1 >= 0.5:
        r_number = (((number * (10**ndigits))//1) + 1)/(10**ndigits)
    else:
        r_number = ((number * (10**ndigits))//1)/(10**ndigits)
    return r_number


n = float(input('Введите десятичное число: '))
d = int(input('Введите количество знаков: '))

r = my_round(n, d)
print(r)

###############################################################

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

import random
import string

print('\n')
print('Задача-2\n')


def lucky_ticket(ticket_number):
    el = []
    for i in range(len(ticket_number)):
        el.append(int(ticket_number[i]))
    s_p1 = sum(el[0:int(len(ticket_number)/2)])
    s_p2 = sum(el[int(len(ticket_number)/2):])
    if s_p1 == s_p2:
        res = 1
    else:
        res = 0
    return res


t_size = int(input('Введите количество знаков в билете: '))
t_num = ''.join([random.choice(string.digits) for n in range(t_size)])
# t_num = '17233217'
print('Ваш билет: ', t_num)

t_status = lucky_ticket(t_num)

if t_status == 1:
    print('\nБилет счастливый!')
else:
    print('\nБилет обычный...')

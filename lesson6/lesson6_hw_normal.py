# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

import libs.lesson6_hw_normal_lib as normal_lib


kids = [normal_lib.Schoolkid('Иванов', 'А.В.', ['Иванова И.М.', 'Иванов В.С.'], '1А', ['Математика', 'Чтение', 'Физкультура']),
        normal_lib.Schoolkid('Петрова', 'М.Е.', ['Петрова С.Н.', 'Петров Е.А.'], '1А', ['Математика', 'Чтение', 'Физкультура']),
        normal_lib.Schoolkid('Сидоров', 'С.Б.', ['Сидорова А.М.', 'Сидоров Б.П.'], '1А', ['Математика', 'Чтение', 'Физкультура']),
        normal_lib.Schoolkid('Шишкина', 'О.Г.', ['Шишкинаа В.Р.', 'Шишкин Г.М.'], '2А', ['Математика', 'Чтение', 'Физкультура', 'Английский']),
        normal_lib.Schoolkid('Сорокин', 'А.Д.', ['Сорокина Н.М.', 'Сорокин Д.К.'], '2А', ['Математика', 'Чтение', 'Физкультура', 'Английский']),
        normal_lib.Schoolkid('Воробьева', 'Е.В.', ['Воробьева М.В.', 'Воробьев В.Д.'], '2А', ['Математика', 'Чтение', 'Физкультура', 'Английский']),
        normal_lib.Schoolkid('Бобров', 'С.А.', ['Боброва В.П.', 'Бобров А.Н.'], '3А', ['Математика', 'Чтение', 'Физкультура', 'Английский', 'История']),
        normal_lib.Schoolkid('Волкова', 'А.С.', ['Волкова З.М.', 'Волков С.К.'], '3А', ['Математика', 'Чтение', 'Физкультура', 'Английский', 'История']),
        normal_lib.Schoolkid('Нестеров', 'К.А.', ['Нестерова В.С.', 'Нестеров А.Р.'], '3А', ['Математика', 'Чтение', 'Физкультура', 'Английский', 'История'])]

teachers = [normal_lib.Teacher('Косыгин', 'П.А.', 'Математика'),
            normal_lib.Teacher('Головина', 'М.Д.', 'Чтение'),
            normal_lib.Teacher('Чуриков', 'В.М.', 'Физкультура'),
            normal_lib.Teacher('Сурикова', 'А.Н.', 'Английский'),
            normal_lib.Teacher('Белов', 'Н.Б.', 'История')]


# 1. Получить полный список всех классов школы
class_ids_raw = []
for _ in kids:
    class_ids_raw.append(_.get_class_id())
class_ids = list(set(class_ids_raw))
print('1. Классы школы: ', class_ids)

# 2. Получить список всех учеников в указанном классе
class_id = '2А'
kids_list = []
kids_list_raw = []
for _ in kids:
    kids_list_raw.append(_.get_class_kids_list())
for _ in kids_list_raw:
    if _[1] == class_id:
        kids_list.append(_[0])
print(f'2. Ученики класса {class_id}: ', kids_list)

# 3. Получить список всех предметов указанного ученика
kid_full_name = 'Волкова А.С.'
kid_subj = []
kid_subj_raw = []
for _ in kids:
    kid_subj_raw.append(_.get_kid_subj_list())
for _ in kid_subj_raw:
    if _[0] == kid_full_name:
        kid_subj.append(_[1])
print(f'3. Предметы ученика {kid_full_name}: ', kid_subj)

# 4. Узнать ФИО родителей указанного ученика
kid_full_name = 'Сорокин А.Д.'
kid_parent = []
kid_parent_raw = []
for _ in kids:
    kid_parent_raw.append(_.get_parent_list())
for _ in kid_parent_raw:
    if _[0] == kid_full_name:
        kid_parent.append(_[1])
print(f'4. Родители ученика {kid_full_name}: ', kid_parent)

# 5. Получить список всех Учителей, преподающих в указанном классе
class_id = '2А'
class_subj_list = []
class_subj_list_raw = []
teacher_list = []
teacher_list_raw = []
for _ in kids:
    class_subj_list_raw.append(_.get_class_subj_list())
for _ in class_subj_list_raw:
    if _[0] == class_id:
        class_subj_list.append(_[1])
        break
for _ in teachers:
    teacher_list_raw.append(_.get_teachers_list())
for i in teacher_list_raw:
    for j in class_subj_list:
        for k in j:
            if i[1] == k:
                teacher_list.append(i[0])
print(f'5. Учителя класса {class_id}: ', teacher_list)

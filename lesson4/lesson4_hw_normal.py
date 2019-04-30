# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re
import random
import os
import string

print('\nЗадача-1')

line1 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
        'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
        'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
        'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
        'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
        'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
        'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
        'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
        'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
        'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
        'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
        'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
        'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
        'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
        'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

print('Через re\n')

found_not_letter = re.findall(r'[^a-z,A-Z]', line1)
if len(found_not_letter) == 0:
       found1 = re.findall(r'[a-z]+', line1)
       for i in range(0, len(found1), 30):
              print(found1[i:i+30])
       else:
# ! Корректно работает только с данной конкретной строкой (не содержащей иных символов,
# кроме латинских букв в верхнем и нижнем регистре).
              pass


print('\nБез re')

ascii_u = list(map(lambda x: chr(x), list(range(65, 91))))
ascii_l = list(map(lambda x: chr(x), list(range(97, 123))))

list1 = list(line1)
for el_ascii_u in ascii_u:
       for i, el_list1 in enumerate(list1):
              if el_ascii_u == el_list1:
                     list1[i] = '-'

str1 = ''.join(list1).split('-')
found2 = [el for el in str1 if el != '']
for i in range(0, len(found2), 30):
       print(found2[i:i + 30])

# ! Корректно работает только с данной конкретной строкой (не содержащей иных символов,
# кроме латинских букв в верхнем и нижнем регистре).


###############################################################

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAM2kgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

print('\n')
print('Задача-2\n')

line2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
        'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
        'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
        'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
        'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
        'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
        'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
        'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
        'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
        'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
        'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
        'KCuUJmGYJZPpRBFNLkq2igxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
        'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
        'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
        'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'


print('Через re')
# line2 = 'GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec'
# так
print(re.findall(r'(?<=[a-z]{2})[A-Z]+(?=[A-Z]{2})', line2))
# или так
print(re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line2))


print('\nБез re')

str_f = ''
sl = []
for i in line2:
        if i.islower():
                str_f += '_'
        if i.isupper():
                str_f += '-'

for i in range(len(str_f)):
        str2 = ''
        if i < len(str_f) - 2:
                if str_f[i] == '_' and str_f[i+1] == '_' and str_f[i+2] == '-':
                        str2 += str_f[i] + str_f[i+1] + str_f[i+2]
                        for j in range(i+2, len(str_f)):
                                if str_f[j] == '_':
                                        break
                                else:
                                        str2 += str_f[j]
                        if len(str2) >= 6:
                                sl.append([i, j])

res = []
for i in sl:
        res.append(line2[i[0]+2:i[1]-2])
print(res)


###############################################################

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

print('\n')
print('Задача-3\n')


EL_Q = 2500


def w_file(f_dir, f_name):
    path = os.path.join(f_dir, f_name)
    str_tmp = ''.join([random.choice(string.digits) for n in range(EL_Q)])
    with open(path, 'w') as f:
        f.write(str_tmp)


def cl_file(f_dir, f_name):
    path = os.path.join(f_dir, f_name)
    str_tmp = ''
    with open(path, 'w') as f:
        f.write(str_tmp)


def find_max_seq(f_dir, f_name):
    path = os.path.join(f_dir, f_name)
    with open(path, 'r') as f:
        seq = f.readline()
        max_seq = ''
        tmp_seq = ''
        for i in seq:
            if i not in tmp_seq:
                if len(max_seq) < len(tmp_seq):
                    max_seq = tmp_seq
                tmp_seq = ''
            tmp_seq = tmp_seq + i
#            print(tmp_seq)
    return max_seq


# f_dir = input('Введите имя директории: ')
# f_name = input('Введите имя файла: ')
f_dir = 'data'
f_name = 'tmp.txt'
w_file(f_dir, f_name)
print('Найденная максимальная последовательность: ', find_max_seq(f_dir, f_name))
cl_file(f_dir, f_name)

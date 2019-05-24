#

import os
import sqlite3
import datetime
import json
import requests
import urllib.request
import gzip
import shutil

'''
0. Загрузка и распаковка архива
'''
DIR = 'data'
'''
urllib.request.urlretrieve('http://bulk.openweathermap.org/sample/city.list.json.gz', 'city.list.json.gz')
with gzip.open('city.list.json.gz', 'rb') as f_in:
    with open('city.list.json', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
'''
'''
1. Создание файла базы данных SQLite с заданной схемой
Для отладки список городов скачан вручную, сокращен до 5 и размещен в отдельном каталоге
'''

r_json = dict.fromkeys(['id', 'name', 'country', 'coord'])

with open(os.path.join(DIR, 'city.list.json'), 'r', encoding='UTF-8') as f:
    r_json = json.load(f)

with open(os.path.join(DIR, 'app.id'), 'r', encoding='UTF-8') as f2:
    app_id = f2.readline()

t3_city = []
for _ in range(len(r_json)):
    l_city = dict(r_json[_])
#    print(l_city)
    req = str('http://api.openweathermap.org/data/2.5/weather?id=') \
        + str(l_city['id']) \
        + str('&units=metric&appid=') \
        + str(app_id)
    res = requests.get(req)
    t1_city = json.loads(res.text)
#    print(t1_city)
    t2_city = {}
    for key, value in t1_city.items():
        if key == 'id':
            t2_city.update({key: value})
        elif key == 'name':
            t2_city.update({key: value})
        elif key == 'main':
            t1_d = dict(value)
            for key2, value2 in t1_d.items():
                if key2 == 'temp':
                    t2_city.update({key2: value2})
        elif key == 'weather':
            for _ in value:
                t2_d = dict(_)
                for key3, value3 in t2_d.items():
                    if key3 == 'id':
                        t2_city.update({'weather_' + key3: value3})
    t3_city.append(t2_city)
# print(t3_city)

f_db = 'weather.db'
conn = sqlite3.connect(f_db)
conn.close()

os.remove(f_db) # удаляет текущий файл db, добавить ветвление на случай наличия файла
with sqlite3.connect(f_db) as c:
    c.execute('CREATE TABLE weather (city_id INTEGER PRIMARY KEY, city VARCHAR(255), date date, temp FLOAT, weather_id INTEGER);')
for _ in t3_city:
    with sqlite3.connect(f_db) as c:
        c.execute('INSERT INTO weather VALUES (?,?,?,?,?)', [_['id'], _['name'], datetime.date.today(), _['temp'], _['weather_id']])


'''
2. Вывод списка стран и выбор страны для дальнейших действий
'''

d_country = []
for _ in range(len(r_json)):
    l_country = dict(r_json[_])
    print(l_country)
    for key, value in l_country.items():
        if key == 'country':
            d_country.append(value)
print('Список стран:\n', d_country)

set_country = input('Введите код страны: ')


'''
3. Получение JSON для городов выбранной страны и запись данных в JSON-файлы с погодой для этих городов 
'''

l_c_id = []
c_id = 0
for _ in range(len(r_json)):
    l_country = dict(r_json[_])
    for key, value in l_country.items():
        if key == 'id':
            c_id = value
        if value == set_country:
            l_c_id.append(c_id)
print(l_c_id)
f_names = []
for _ in l_c_id:
    req = str('http://api.openweathermap.org/data/2.5/weather?id=') \
        + str(_) \
        + str('&units=metric&appid=') \
        + str(app_id)
    res = requests.get(req)
    print(res)
    res_dict = json.loads(res.text)
    print(type(res_dict))
    res_json = json.dumps(res_dict, indent=4, separators=(',', ': '))
    print(type(res_json))
    print(res_json)
    f_name = str(_) + str('.json')
    f_names.append(f_name)
    with open(os.path.join(f_name), 'w') as f_wr:
        f_wr.write(res_json)

'''
4. Парсинг JSON и запись в базу
Доделать!..
'''

print('\n', f_names)
t3_city = []
for _ in f_names:
    with open(os.path.join(_), 'r', encoding='UTF-8') as f_r:
        f_read = dict(json.load(f_r))
        print(type(f_read))
        print(f_read)
        t2_city = {}
        for key, value in f_read.items():
            if key == 'id':
                t2_city.update({key: value})
            elif key == 'name':
                t2_city.update({key: value})
            elif key == 'main':
                t1_d = dict(value)
                for key2, value2 in t1_d.items():
                    if key2 == 'temp':
                        t2_city.update({key2: value2})
            elif key == 'weather':
                for _ in value:
                    t2_d = dict(_)
                    for key3, value3 in t2_d.items():
                        if key3 == 'id':
                            t2_city.update({'weather_' + key3: value3})
        t3_city.append(t2_city)
print(t3_city)

# f_db = 'weather.db'
# conn = sqlite3.connect(f_db)
# conn.close()

# os.remove(f_db) # удаляет текущий файл db, добавить ветвление на случай наличия файла
for _ in t3_city:
    with sqlite3.connect(f_db) as c:
        # поменять sql-запрос на update
        c.execute('INSERT INTO weather VALUES (?,?,?,?,?)', [_['id'], _['name'], datetime.date.today(), _['temp'], _['weather_id']])


'''
+ Рефакторинг кода (сделать классы, либо функции)
Доделать!..
'''
'''
+ Скрипт экспорта из базы в JSON/CSV
Доделать!..
'''
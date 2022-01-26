# JSON - Java Script Object Notation, работает со всеми языками программирования, структура файла похожа на словарь

# https://vk.com/dev/users.getFollowers?params[user_id]=66748&params[count]=2&params[fields]=photo_50&params[v]=5.130

import json  # импортируем встроенный модуль


''' 1. Как распарсить имеющийся файл '''

str_json = """ 

{
    "response": {
            "count": 39987,
            "items": 
                  [{"first_name": "Евгений",
                    "id": 634387267,
                    "last_name": "Морозов",
                    "can_access_closed": true
                    },
                    {
                    "first_name": "Tom",
                    "id": 645815022,
                    "last_name": "Vov",
                    "can_access_closed": true
                     }]
                  }
}

"""
print('Тип данных str_json ', type(str_json))

data = json.loads(str_json)  # метод для загрузки json в Питон
print('Тип данных data ', type(data))
print(data)

# если удаляем строки из текстовой переменной, следим чтобы в конце не было запятой

print(data['response']['items'])
print(type(data['response']['items']))  # тип данных словарь, внутри которого тоже словарь

for item in data['response']['items']:
    print(type(item), item)

for item in data['response']['items']:  # можем обратиться к ключам вложенного словаря
    print(item['first_name'], item['last_name'])


''' 2. Как изменить JSON - файл '''  # 7:42

from random import randint

for item in data['response']['items']:
    del item['id']  # удаляем ключ (уйдет из всех вложенных словарей вместе со значениями)
    item['likes'] = randint(100, 200)  # добавляем ключ вместе со значениями (во все вложенные словари)

print(data['response']['items'])


''' 3. Как перевести в JSON - файл '''  # 8:42

new_json = json.dumps(data, indent=2)  # метод для перевода заготовленных данных в .json,
                                       # indent отвечает за кол-во отступов на каждом уровне вложенности для красивого вывода
print('Тип данных new_json ', type(new_json))  # --> <class 'str'>
print(new_json)

# при вывод \u обозначает, что все русские буквы перекодированы в Unicode
# это не проблема, при преобразовании формата .json в словарь отобразится все корректно


''' 4. Соответствие форматов Python - JSON (соотв.) при переводе 
    
    dict --------- object
    list, tuple -- array
    str	---------- string
    int, float --- number
    True --------- true
    False -------- false
    None --------- null
    
    '''
from datetime import datetime

for item in data['response']['items']:
    item['a'] = None  # добавляем ключ вместе со значениями (во все вложенные словари)
    item['now']=datetime.now().strftime('%d/%m/%y')  # без .strftime('%d/%m/%y') перевод в известный формат
                                                     # строку с указанием формата не сработает, т.к. дататайм неизсестен .json

new_json = json.dumps(data, indent=2)
print(new_json)  # добавится новый ключ "a": null, причем None трансформируется в null


''' 5. Сохранение JSON '''

with open('my.json', 'w') as file:  # создадим в текущей режиссерии файл и откроем его на запись
    json.dump(data, file, indent=3)  # указываем методу данные и путь

# <-- слева в каталоге появился файл


''' 6. Импорт данных из файла JSON без прямой загрузки '''

with open('my.json', 'r') as file:  # откроем на чтение
    data_new = json.load(file)

print(data)
print(type(data))

''' Резюме:
    
    load - считывание файлов json
    loads - считывание строки в формате .json
    dump - создание файла
    dumps - создает строку в формате .json
    
    '''
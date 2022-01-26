''' 1. Подсчет количества баллов
При таком использовании ключи будут являться объектами, а значения ключей - количество появлений этих объектов

'''

#  Задача: посчитать, сколько раз в строке встретилась каждая буква

d = {}  # -- создаем пустой словарь
d['a'] = 1  # -- помещаем в него пару
print(d)

if 'a' in d:  # -- проверяем наличие элемента в словаре
    d['a'] += 1  # -- если да, то увеличиваем на 1 значение
else:
    d['a'] = 1  # -- если нет, создаем ключ со значением 1
print(d)

s = 'sadjsdjfjdlvjdfjvnjxhdfjvn'
d = {}
for i in s:
    if i.isalpha():  # -- проверяем, точно ли буква, а не символ
        if i in d:  # -- проверяем наличие элемента в словаре
            d[i] += 1  # -- если да, то увеличиваем на 1 значение
        else:
            d[i] = 1  # -- если нет, создаем ключ со значением 1
print(d)  # --> {'s': 2, 'a': 1, 'd': 5, 'j': 7, 'f': 3, 'l': 1, 'v': 3, 'n': 2, 'x': 1, 'h': 1}

s = 'sadjsdjfjdlvjdfjvnjxhdfjvn'
d = {}
for i in s:
    if i.isalpha():  # -- проверяем, точно ли буква, а не символ
        d[i] = d.get(i, 0) + 1  # получаем значение пары с ключом i и прибавляем 1,
                                # или создаем новую пару с ключом 0 и прибавляем 1
print(d)  # --> {'s': 2, 'a': 1, 'd': 5, 'j': 7, 'f': 3, 'l': 1, 'v': 3, 'n': 2, 'x': 1, 'h': 1}


''' 2. Замена разреженного списка
Вместо списка из большого количества элементов, в котором предполагается неполное использование элементов
Продолжает задачу выше. А так же улучшает решение задачи из урока ранее, про подсчет кол-ва букв в строке из урока ...
'''

''' 3. Установление связи между объектами
Например, словарь-переводчик.

words = {}
s = 0
while s < 100:
    s = input()
    if s in words:
        print("Слово ", s, 'переводится как', words[s])
    else:
        print("Введите перевод, пжлста: ")
    words[s] = input()
    s += 1
'''

''' 3. Хранение данных об объекте. Внутри словаря еще один словарь с одинаковыми ключами
'''

contacts = {'John Kennedy':
                    {'birthday': '29 may 1917', 'city': 'Brookline', 'phone': None, 'children': 3},
            'Arnold Shwarts':
                    {'birthday': '30 july 1947', 'city': 'Gradec', 'phone': '555-555-555', 'children': 5},
            'Donald Trump':
                    {'birthday': '14 july 1946', 'city': 'New York', 'phone': '777-777-777', 'children': 4}
            }

# создадим лист, в который соберем фамилии
persons = ['John Kennedy', 'Arnold Shwarts', 'Donald Trump']

for person in persons:  # подставим фамилии в качестве ключей и пройдемся циклом по словарю, запросим пары ключ - значение
    print(person, contacts[person]['birthday'])  # contacts[person] - обращение к вложенному словарю
    ''' вывод 
    John Kennedy 29 may 1917
    Arnold Shwarts 30 july 1947
    Donald Trump 14 july 1946
    '''

for person in persons:  # -- внутри цикла достанем всю информацию о человеке
    birthday = contacts[person]['birthday']  # создаем переменные и вносим в них ключи вложенного словаря
    city = contacts[person]['city']
    phone = contacts[person]['phone']
    children = contacts[person]['children']

    print(person, children, phone)
    ''' вывод 
    John Kennedy 3 None
    Arnold Shwarts 5 555-555-555
    Donald Trump 4 777-777-777
    '''

contacts = {'John Kennedy':
                    {'birthday': '29 may 1917', 'city': 'Brookline', 'phone': None, 'children': 3},
            'Arnold Shwarts':
                    {'birthday': '30 july 1947', 'city': 'Gradec', 'phone': '555-555-555', 'children': 5},
            'Donald Trump':
                    {'birthday': '14 july 1946', 'city': 'New York', 'phone': '777-777-777', 'children': 4}
            }

# создадим лист, в который соберем фамилии
persons = ['John Kennedy', 'Arnold Shwarts', 'Donald Trump']


for person in persons:
    print(person)
    for data in contacts[person]:  # обойдем при помощи переменной все данные, что лежат в словаре про человека
        print(data, contacts[person][data])  # обращаемся к вложенному словарю? перебирая его ключи переменной data
    print()
    ''' вывод 
    John Kennedy
    birthday 29 may 1917
    city Brookline
    phone None
    children 3
    '''
'''
Список, состоящий из кортежей. Хранит в себе фамилию и год рождения.
Кортежи нумеруются с нуля, и элементы внутри кортежа тоже.
Например, a[1][1] = 2002
'''

a = [
     ('Sidorov', 1995),
     ('Lukov', 2002),
     ('Petrov', 1991),
     ('Gorbachev', 1984),
     ('Kostin', 2000),
     ('Isaev', 2005),
     ('Eliseev', 1999),
     ('Kozlov', 2004),
     ('Bukov', 1995),
     ('Gavrilov', 1980),
     ('Efremov', 2006),
]

# вынуть все
b = [elem for elem in a]
print(b)  # --> [('Sidorov', 1995), ('Lukov', 2002), ('Petrov', 1991), ('Gorbachev', 1984), ('Kostin', 2000), ('Isaev', 2005), ('Eliseev', 1999), ('Kozlov', 2004), ('Bukov', 1995), ('Gavrilov', 1980), ('Efremov', 2006)]

# вынуть фамилии
c = [elem[0] for elem in a]
print(c)  # --> ['Sidorov', 'Lukov', 'Petrov', 'Gorbachev', 'Kostin', 'Isaev', 'Eliseev', 'Kozlov', 'Bukov', 'Gavrilov', 'Efremov']

# вынуть даты
c = [elem[1] for elem in a]
print(c)  # --> [1995, 2002, 1991, 1984, 2000, 2005, 1999, 2004, 1995, 1980, 2006]

# вынуть все фамилии c условием
d = [elem[0] for elem in a if elem[0].startswith('E')]
print(d)  # --> ['Eliseev', 'Efremov']

# вынуть все первые буквы имен, ДР которых позднее 2000 (можно, т.к. строковые элементы тоже индексируются)
e = [elem[0][0] for elem in a if elem[1] > 2000]
print(e)  # --> ['L', 'I', 'K', 'E']


''' 
Работа со словарями
Ключ - фамилия человека, значение - снова словарь из трех ключей и значений. 
Обращение к элементу словаря возвращает ключи, а обращение непосредственно к ключу вернет значение
'''

a = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
}

# по умолчанию, обращение в словарях идет к ключам
b = [elem for elem in a]
print(b)  # --> ['Sidorov', 'Lukov', 'Petrov', 'Gorbachev', 'Kostin', 'Isaev', 'Eliseev', 'Kozlov', 'Bukov']

# чтобы обратиться к значению ключа, вызовем его по индексу и названию словаря
c = [a[elem] for elem in a]
print(c)  # --> [{'age': 1995, 'hobby': 'soccer', 'car': 'BMW'}, {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'}, {'age': 1991, 'hobby': 'chess', 'car': 'BMW'}, {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'}, {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'}, {'age': 2005, 'hobby': 'music', 'car': 'BMW'}, {'age': 1999, 'hobby': 'chess', 'car': 'Audi'}, {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'}, {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'}]

# чтобы вызвать название авто, сначала обратимся к вложенному словарю, с индексом - его ключ
d = [a[elem]['car'] for elem in a]
print(d)  # --> ['BMW', 'Opel', 'BMW', 'BMW', 'Audi', 'BMW', 'Audi', 'Opel', 'Audi']

# вызвать хобби тех, кто моложе 2000 года
e = [a[elem]['hobby'] for elem in a if a[elem]['age'] < 2000]
print(e)  # --> ['soccer', 'chess', 'tennis', 'chess', 'basketball']

# вызвать фамилии тех, у кого хобби ...
# собираем кортеж из фамилии (она и есть elem), и обращения к клюсу вложенного словаря a[elem]['hobby']
f = [(elem, a[elem]['hobby']) for elem in a]
print(f)  # --> [('Sidorov', 'soccer'), ('Lukov', 'basketball'), ('Petrov', 'chess'), ('Gorbachev', 'tennis'), ('Kostin', 'swimming'), ('Isaev', 'music'), ('Eliseev', 'chess'), ('Kozlov', 'soccer'), ('Bukov', 'basketball')]

g = [(elem, a[elem]['hobby']) for elem in a if a[elem]['age'] < 2000 and a[elem]['hobby'] == 'soccer']
print(g)  # --> [('Sidorov', 'soccer')]

''' 
Строковые переменные
'''

s = '5sd5fsdff5sdfsd21f'

# вынуть из строки все цифры строками методом .isdigit() - вернет True / False
b = [i for i in s if i.isdigit()]
print(b)  # --> ['5', '5', '5', '2', '1']

# вынуть из строки все цифры цифрами .int() и .isdigit() - вернет True / False
bb = [int(i) for i in s if i.isdigit()]
print(bb)  # --> [5, 5, 5, 2, 1]

# вынуть из строки все буквы .isalpha() - вернет True / False
bbb = [i for i in s if i.isalpha()]
print(bbb)  # --> ['s', 'd', 'f', 's', 'd', 'f', 'f', 's', 'd', 'f', 's', 'd', 'f']

''' 
Двумерные списки
'''

n = 5
m = 3
a = [[0] * m for i in range(n)]
print(a)  # --> [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in a:
    print(i)
    ''' вывод 
    [0, 0, 0]
    [0, 0, 0]
    [0, 0, 0]
    [0, 0, 0]
    [0, 0, 0]
    '''

#  random.randint(1,9) --> генерится случайное число
# [random.randint(1,9) for j in range(m)] --> генерится по количеству столбцов
# [[...] for i in range(n)] -->  сгенеренный лист повторяется по кол-ву строк

import random
n = 5
m = 5
b = [[random.randint(1, 9) for j in range(m)] for i in range(n)]
print(b)  # --> [[5, 4, 1, 6, 8], [5, 2, 5, 8, 8], [5, 6, 8, 7, 5], [3, 9, 1, 2, 1], [7, 9, 3, 2, 1]]
for i in b:
    print(i)
    ''' вывод
    [5, 4, 1, 6, 8]
    [5, 2, 5, 8, 8]
    [5, 6, 8, 7, 5]
    [3, 9, 1, 2, 1]
    [7, 9, 3, 2, 1]
    '''

# вытянем элементы главной диагонали
# перебираем листы (главные элементы), потом их внутренние элементы, ограничиваем условием

c = [b[i][j] for i in range(n) for j in range(m) if i == j]
print('main', c)  # --> main [5, 2, 8, 2, 1]

# выведем все элементы 2 строки, i не меняется
d = [b[2][j] for j in range(m)]
print(d)  # --> [5, 6, 8, 7, 5]

# выведем все элементы 2 строки, i не меняется
e = [b[i][3] for i in range(n)]
print(e)  # --> [6, 8, 7, 2, 2]

''' 
Выведем таблицу умножения
'''

# не  забываем вложить один генератор в другой, иначе будет просто последовательность цифр
n = 9
m = 9
e = [[i * j for i in range(1, n + 1)] for j in range(1, m + 1)]
for i in e:
    print(i)
    ''' вывод
    [1, 02, 03, 04, 05, 06, 07, 08, 09]
    [2, 04, 06, 08, 10, 12, 14, 16, 18]
    [3, 06, 09, 12, 15, 18, 21, 24, 27]
    [4, 08, 12, 16, 20, 24, 28, 32, 36]
    [5, 10, 15, 20, 25, 30, 35, 40, 45]
    [6, 12, 18, 24, 30, 36, 42, 48, 54]
    [7, 14, 21, 28, 35, 42, 49, 56, 63]
    [8, 16, 24, 32, 40, 48, 56, 64, 72]
    [9, 18, 27, 36, 45, 54, 63, 72, 81]
    '''
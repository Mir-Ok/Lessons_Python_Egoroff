'''
Кортеж - неизменемая последовательность, обычно используемая для хранения рахнотоипных объектов.
По сути, похож на список, много общих функций и методов, но прахница в НЕИЗМЕНЯЕМОСТИ
'''

# ---------------------------------------
# создание кортежа

a = (1, 2, 3, 4, 5)
print(a, type(a))  # --> (1, 2, 3, 4, 5) <class 'tuple'>

a = 1, 2, 3, 4, 5  # --> аналогично выше, но без скобок
print(a, type(a))  # --> (1, 2, 3, 4, 5) <class 'tuple'>

a = 1,  # --> даже один элемент и запятая уже создают кортеж, иначе просто переменная
print(a, type(a))  # --> (1,) <class 'tuple'>

a = tuple()  # --> пустой кортеж
print(a, type(a)) # -->  () <class 'tuple'>

a = tuple([1,2,3])  # --> из итерабельной последовательности - из листа
print(a, type(a))  # -->  <class 'tuple'>

a = tuple(range(3))  # --> из итерабельной последовательности - из range
print(a, type(a))  # -->  (0, 1, 2) <class 'tuple'>

a = tuple((1,2,3))  # --> из итерабельной последовательности - из кортежа
print(a, type(a))  # -->  (0, 1, 2) <class 'tuple'>


# ---------------------------------------
# функции кортежа

# _1 длина
a = (1, 2, 3, 4, 5)
print(len(a))  # --> 5

# _2 вхождение / НЕвхождение
a = (1, 2, 3, 4, 5)
print(2 in a)  # --> True
print(2 in a, 3 in a, 8 in a)  # --> True True False
print(2 not in a)  # --> False

# _3 сцепление (складывание) кортежей
a = 1,2,3
b = 4,5
print(a+b)  # --> (1, 2, 3, 4, 5)
print(b+a)  # --> (4, 5, 1, 2, 3)

# _4 дублирование кортежей
a = 1,2,3
print(a*2)  # --> (1, 2, 3, 1, 2, 3)
#  a = 1,2,3
# print(a + 2)  # --> TypeError: can only concatenate tuple (not "int") to tuple

# _5 сравнение внутри кортежей из однотипных элементов? если будут разнотипные - выдаст ошибку
a = 1,2,3
b = 4,5
print(min(a), max(b))  # --> 1 5

# _6 суммирование
b = 4,5
print(sum(b))  # --> 9

# _7 преобразование в список
b = 4,5
b = list(b)
print(b)  # --> [4, 5]


# ---------------------------------------
# методы кортежа (их 2), только неизменяющие, в разы меньше, чем у списков

a = 1, 'hello', 3, 54, False, 5
print(a[1])  # --> hello
# a[1] = 'hi' вызовет ошибку, т.к. неизменяемый объект

# _1 поиск индекса элемента
print(a.index(1))  # --> 0 индекс имеет элемент со значением 1

# _2 подсчет, сколько раз элемент в кортеже
print(a.count(3))  # --> 1

''' ВАЖНО! 
Хотя сам кортеж - это неизменяемый объект, внутри него могут находиться изменяемые.
Элемент кортежа - список, может быть изменен
'''
a = 1, 'hello', 3, 54, False, 5, [1,2,3]
a[6].append(8)
print(a)  # --> (1, 'hello', 3, 54, False, 5, [1, 2, 3, 8])


# ---------------------------------------
# использование

# _1 гарантия неизменяемости элементов
a = [1, 'hello', 3, 54, False, 5, [1,2,3]]
b = a
print(a)  # --> [1, 'hello', 3, 54, False, 5, [1, 2, 3]]
print(b)  # --> [1, 'hello', 3, 54, False, 5, [1, 2, 3]]

b[2] = 100  # изменение объекта повлечет за собоц изменение во всех списках, которые на него ссылаются
print(a)  # --> [1, 'hello', 100, 54, False, 5, [1, 2, 3]]
print(b)  # --> [1, 'hello', 100, 54, False, 5, [1, 2, 3]]

# _2 кортежи занимают меньше места, чем списки, быстрее обрабатываются
a = [1, 'hello', 3, 54, False, 5, [1,2,3]]
b = tuple([1, 'hello', 3, 54, False, 5, [1,2,3]])
print(a.__sizeof__())  # --> 96
print(b.__sizeof__())  # --> 80

# _3 кортежи могут использоваться как ключи словаря
a = (1,2,3)
b = {}
b[a] = 'hello'
print(b)  # --> {(1, 2, 3): 'hello'}

# _4 кортежи можно обходить циклом по значениям и индексам (т.к. упорядоченая последовательноть)
a = (1, 'hello', 3, 54, False, 5, [1,2,3])
for i in a:
    print(i)  # по значениям
    '''
    1
    hello
    3
    54
    False
    5
    [1, 2, 3]
    '''

a = (1, 'hello', 3, 54, False, 5, [1,2,3])
for i in range(len(a)):
    print(i, a[i])  # по индексам и значениям
    '''
    0 1
    1 hello
    2 3
    3 54
    4 False
    5 5
    6 [1, 2, 3]
    '''
'''
Множество (set) неупорядоченная коллекция уникальных элементов, повтряющиеся значения отсутствуют.
Целые числа, строки и другие НЕизменяемые объекты (кортеж). Вложить список списков в множество нельзя
'''

# --- создание

a = {1,2,3}
print(a, type(a))  # ---> {1, 2, 3} <class 'set'>

a1 = {1,2,3,1,2,3}
print(a1, type(a1))  # ---> {1, 2, 3} <class 'set'>, работу по отслеживаю и удалению дублей объект совершает сам

d = {'abracadabra'}
print(d, type(d))  # ---> {'abracadabra'} <class 'set'>

c = set([1,2,3])  # ---> преобразование из листа функцией
print(c, type(c))  # ---> {1, 2, 3} <class 'set'>

d1 = set('abracadabra')  # ---> преобразование из строки функцией
print(d1, type(d1))  # ---> {'b', 'c', 'r', 'a', 'd'} <class 'set'>, разбивает на элементы и удаляет дубли, не упорядочивает

e = set(range(5))
print(e)  # ---> {0, 1, 2, 3, 4}

# z = set([[1,2], [3,4], [1,2], [2,1]])
# print(z)  # ---> TypeError: unhashable type: 'list' - нельзя использовать изменяемые объекты!

# вывод пустого множества, ВАЖНО только через ФУНКЦИЮ, через f = {} создается СЛОВАРЬ
f = set()
print(f, type(f))  # --> set() <class 'set'>

# ------------------------------------
# добавление элемента, попытка добавить дубль ни к чему не приводит

a = {54, 32, 54, 3, 4, 2}
a.add(9)
print(a)  # --> {32, 2, 3, 4, 9, 54}

a.update([5, 6, 4, 3])  # --> метод принимает итерабельную последовательность (список), добавляет поэлементно
print(a)  # --> {32, 2, 3, 4, 5, 6, 9, 54}

a.update('hello')  # --> метод принимает итерабельную последовательность (строки), добавляет поэлементно
print(a)  # --> {32, 2, 3, 4, 5, 6, 9, 'e', 'l', 'o', 'h', 54}

a.update(range(5))  # --> метод принимает итерабельную последовательность (range), добавляет поэлементно
print(a)  # --> {32, 0, 2, 3, 4, 5, 6, 'o', 1, 9, 'h', 'l', 'e', 54}

a.update({12, 14, 22})  # --> метод принимает итерабельную последовательность (множество), добавляет поэлементно
print(a)  # --> {32, 'o', 2, 3, 4, 5, 6, 0, 1, 9, 12, 14, 'l', 54, 'h', 22, 'e'}

'''  .update() по смыслу равен нескольким повторам .add()  '''

# ------------------------------------
# удаление элемента, попытка добавить дубль ни к чему не приводит

a.discard(32)  # --> если элемента итак нет, ошибку НЕ выдает
print(a)  # --> {0, 2, 3, 4, 5, 6, 'h', 'l', 9, 1, 'e', 12, 14, 54, 22, 'o'}

a.remove(54)  # --> если элемента итак нет, ошибку выдает
print(a)  # --> {0, 2, 3, 4, 5, 6, 'h', 'l', 9, 1, 'e', 12, 14, 22, 'o'}

# a.remove(54)  # --> если элемента итак нет, ошибку выдает
# print(a)  # --> KeyError: 54

a.pop()  # --> т.к. неупорядочено, удаляет не последний, а случайный элемент и возвращает его.
         # Из пустого множества удаление вызывает ошибку

a.clear()
print(a)  # --> set()

# ------------------------------------
# операции над множествами

b = {32, 2, 3, 4, 5, 6, 9, 'e', 'l', 'o', 'h', 54}

# _ 1 длина множества
print(len(b))  # --> 12

# _ 2 наличие указанного элемента в множестве
print(4 in b)  # --> True
print(4 in b, 7 in b)  # --> True False
print(4 in b, 7 not in b)  # --> True True

# _ 3 пересечение множеств
c = {1,2,3,4}
d = {3,4,5,6}
f = {10,11,12}
e = c & d  # пересечение множеств, общие элементы
g = c & f  # пересечение множеств, общие элементы
print(e)  # -- {3, 4}
print(g)  # -- set() пустое множество, пересечений нет
print(c.intersection(d))  # -- {3, 4} аналог значка &

# _ 4 замена значения исходного множества на пересечение
print(c.intersection_update(d))  # -- команда print(c & = d) устарела

# _ 5 объединение множеств
c = {1,2,3,4}
d = {3,4,5,6}
j = c.union(b)
print(j)  # -- > {1,2,3,4,5,6}, исходное множество не изменяется, только через присвоение

v = {1,2,3,4}
w = {3,4,5,6}
v |= w
print(v)  # -- > {1,2,3,4,5,6} способ изменения исходного множества через объединение

# _ 6 вычитание множеств
v = {1,2,3,4}
w = {3,4,5,6}
print(v-w)  # --> {1, 2} останутся только те, что не присутствуют в вычитаемом множестве,
            # исходное неменяется, чтобы изменить пишем v -= w

# _ 7 симметричные разности
v = {1,2,3,4}
w = {3,4,5,6}
print(v ^ w)  # --> {1, 2, 5, 6} войдут элементы, не пересекающиеся во множествах

# _ 8 сравнение множеств
v = {1,2,3,4}
w = {3,4,5,6}
print(v == w)  # --> False потому что они не равны по элементам, хотя равны по длине (с учетом выброса дублей), порядок не важен

# _ 9 сравнение множеств
v = {1,2,3,4}
w = {3,4,5,6}
print(v > w)  # --> False? потому что w не содержится  в v

v = {1,2,3,4}
w = {1,2,3}
print(v > w)  # --> True, потому что w полностью помещается в v

v = {1,2,3,4}
w = {1,2,3}
print(v >= w)  # --> True, потому что w полностью помещается в v


# _ 10 обход значений циклом, по индексам нельзя, т.к. элемент неупорядочены, print(a[0]) не срабатывает

a = {4,3,2,1}
for i in a:
    print(i)

# ------------------------------------
# задача: посчитать, сколько уникальных слов ввел пользователь

text = input()
a = set()
while text != '':  # -------- пока не ввели пустоту
    slova = text.split()  # - разбиваем поэлементно введенное и помещаем в переменную
    a.update(slova)  # ------ добавляем во множество, повторы отсечет само
    print(a)
    text = input()  # ------- запрашиваем новый ввод
print(len(a))

'''  Позволяет сформировать конечную арифметическую прогрессию

Общий вид: range(a,b,c), где
    a - с какого числа стартовать (включительно),
    b - до какого числа (НЕвключительно),
    с - шаг (по умолчанию +1)

'''

# простой вызов вернет нам саму функцию

print(range(5))         # --> range(0, 5)
print(type(range(5)))   # --> <class 'range'> существует отдельный класс под нее

print(list(range(5)))   # --> [0, 1, 2, 3, 4] - от 0 до правой границы НЕвключительно,
                        # число элементов равно указанному в скобках

print(list(range(0)))   # --> []
print(list(range(-5)))  # --> [], связано с тем, что по умолчанию формируется возрастающая арифм. прогрессия

print(list(range(10, 20)))     # --> [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list(range(10, 20, 2)))  # --> [10, 12, 14, 16, 18]

# Начальное число должно быть меньше конечного, иначе пустой лист
print(list(range(10, 5)))     # --> []

# Шаг можно изменить на отрицательный
print(list(range(10, 0, -1)))  # --> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] снова 0 не входит, т.к. правая граница

''' Возможности использования '''

print(sum(range(5)))  # --> 10 = 0 + 1 + 2 + 3 + 4 сумма всех чисел интервала
print(len(range(5)))  # --> 5 количество чисел в интервале

a, b, c = range(3)  # -- >  множественное присвоение
print(a)  # --> 0
print(b)  # --> 1
print(c)  # --> 2

r = range(7)  # -- >  создание списков
print(r)        # --> range(0, 7)
print(list(r))  # --> [0, 1, 2, 3, 4, 5, 6]
print(r[0])     # --> 0
print(r[6])     # --> 6

''' 
Объект, возвращаемый функцией range() является ИТЕРИРУЕМЫМ, 
т.е. предоставляющим возможность поочередного прохода по своим элементам и поддерживает функцию next().
Итератор помнит, на каком объекте мы сейчас находимся, и при вызове next() соотв. выдает следующий

'''

v = iter(range(5))  # --> функция - итератор
print(v)  # --> <range_iterator object at 0x0000015D1CCB6BD0>

print(next(v))  # --> 0 вызовется первый элемент, т.к. до этого еще ни один не вызывался
print(next(v))  # --> 1
print(v.__next__())  # --> 2 аналогичный функционал, другая форма записи next()
print(v.__next__())
print(next(v))
# print(next(v))  # --> ничего не выдает, кончились элементы, раньше была ошибка? сейчас просто вешает программу

# Посмотрим отдельно функцию итерируемость и next()

n = iter([43, True, 'hello'])  # итерируем список
print(next(n))  # --> 43
print(next(n))  # --> True
print(next(n))  # --> 'hello'

m = iter('hello')  # итерируем строку
print(next(m))  # --> h
print(next(m))  # --> e
print(next(m))  # --> l
print(next(m))  # --> l
print(next(m))  # --> o

m1 = iter(25)    # итерируем число, не выходит, т.к. в памяти это просто одно большое значение
print(next(m1))  # --> TypeError: 'int' object is not iterable

''' В цикле for функция next() вызывается автоматически'''

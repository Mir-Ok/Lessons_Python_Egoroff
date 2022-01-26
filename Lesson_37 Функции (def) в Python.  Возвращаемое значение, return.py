''' Возврат - выдача функцией вместо себя значения, которое можно присвоить переменной

Любая функция имеет параметр return, по умолчанию None, можно перезадать вручную'''

# встроенные функции

a = abs(-7)
b = max(4, abs(-90), 4, min(100,200))  # раскрытие скобок как в математике
print(b)  # --> 100

# самописные функции
def square(x):
    print(x**2)
a = square(6)
print(a)
''' вывод 
36
None
'''

def square(x):
    return x**2  # заменим print на return
a = square(6)
print(a)
''' вывод 
36
None
'''

# работа с return дает возможность вложенного вызова функции
a = square(square(3))
print(a)
''' вывод: 81 '''

def example():
    print(1)
    print(2)
    return 'hello'
    print(4)  # после него ничего не работает, после него автоматический выход из функции, аналог break
    print(5)
example()
''' вывод: 1 2 '''
''' hello не вывелось на экран, потому что мы ничего не сделали с возвращенным значением '''
print(example())
''' вывод: hello '''

# Пример: напишем функцию, которая возвращает четность / нечетность числа. И постепенно оптимизируем ее
def even(x):
    if x%2 == 0:
        return True
    if x%2 != 0:
        return False

for i in range(1,7):
    print(i, even(i))
    ''' вывод: 
    1 False
    2 True
    3 False
    4 True
    5 False
    6 True
    '''

def even(x):
    if x % 2 == 0:
        return True
    return False  # можно сократить запись, т.к. если сработает первое условие, то функция прервется

for i in range(1,7):
    print(i, even(i))
    ''' вывод: 
    1 False
    2 True
    3 False
    4 True
    5 False
    6 True
    '''

def even(x):
    return x % 2 == 0  # вернет True, если верно и False, если нет

for i in range(1,7):
    print(i, even(i))
    ''' вывод: 
    1 False
    2 True
    3 False
    4 True
    5 False
    6 True
    '''

# Задача: написать формулу количества сочетаний k элементов в множестве n.
# Для этого пишем формулу факториала

def factorial(x):
    pr = 1
    for i in range(2, x + 1):
        pr = pr * i
    return pr

def sochet(n,k):
    return factorial(n)/(factorial(k) * factorial(n-k))
print(sochet(5,3))
''' вывод: 10 '''

# Задача: написать функцию, которая возвращает два значения

def sqAndPer(a,b):
    return a*b, 2*(a+b)  # вернет в виде кортежа

print(sqAndPer(2,3), type(sqAndPer(2,3)))
''' вывод: (6, 10) <class 'tuple'> '''

square, perimetr = sqAndPer(2,3)  # пользуемся возможностью множественного присвоения
print(square, perimetr)
''' вывод: 6, 10 '''

# если мы хотим возврат ответов в виде списка, мы можем немного изменить код

def sqAndPer(a,b):
    mas = []
    mas.append(a*b)
    mas.append(2*(a+b))
    return mas   # вернет в виде списка

print(sqAndPer(2,3))
''' вывод: [6, 10] '''
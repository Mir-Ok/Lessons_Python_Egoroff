a = [10, 20, 30, 40]
b = [100, 200, 300, 400]

print(enumerate(a))  # --> <enumerate object at 0x000001A4291E2C80>

print(list(enumerate(a)))  # --> [(0, 10), (1, 20), (2, 30), (3, 40)] список кортежей из индекса элемента и его значения

for para in enumerate(a):
    print(para)
    ''' вывод 
    (0, 10)
    (1, 20)
    (2, 30)
    (3, 40)
    '''

# так как выводится кортеж из 2 значений (всегда двух), можем обратиться к ним сразу отдельно
for index, value in enumerate(b):
    print(index, value +1)
    ''' вывод 
    (0, 10)
    (1, 20)
    (2, 30)
    (3, 40)
    '''

# обратите внимание, что при попытке изменить значение внутри цикла, значение останется неизменным,
# либо надо обращаться по индексу, не value +=1, a[index] +=1, причем порядковый номер неизменен
# и стабильно увеличивается на 1

c = 'hello'
for index, value in enumerate(c):
    print(index, value)
    ''' вывод 
    0 h
    1 e
    2 l
    3 l
    4 o
    '''

c = ('hello', 'world')
for index, value in enumerate(c):
    print(index, value)
    ''' вывод 
    0 hello
    1 world
    '''

c = {'hello':1, 'world':2, 'hi':3}  # можем обойти только ключи, причем неизвестно в каком порядке
for index, value in enumerate(c):
    print(index, value)
    ''' вывод 
    0 hello
    1 world
    2 hi
    '''

for index, value in enumerate(range(10, 15)):
    print(index, value)
    ''' вывод: 
    0 10
    1 11
    2 12
    3 13
    4 14
    '''

# у функции enumerate есть второй аргумент, после объекта мы можем передать стартовый номер

c = {'hello' : 1, 'world' : 2, 'hi' : 3}  # можем обойти только ключи, причем неизвестно в какойм порядке
for index, value in enumerate(c, 10):
    print(index, value)
    ''' вывод 
    10 hello
    11 world
    12 hi
    '''
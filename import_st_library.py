import pprint  # модуль красивой печати pretty print

def say_hello(name):
    print(f'Hello, {name}')

def summa(*args):
    return sum(args)

def factorial(n):
    pr = 1
    for i in range(1,n+1):
        pr *= i
    return pr

my_str = 'you are breathtaking!'
my_mum1 = 2
my_num2 = 3

pprint.pprint(locals())  # красиво выведет словарь, содержащий все адреса и имена

''' вывод 
    {'__annotations__': {},
     '__builtins__': <module 'builtins' (built-in)>,
     '__cached__': None,
     '__doc__': None,
     '__file__': 'D:/1_Python/Уроки Egoroff/import_st_library.py',
     '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001C557A10880>,
     '__name__': '__main__',
     '__package__': None,
     '__spec__': None,
     'factorial': <function factorial at 0x000001C557EB6430>,
     'my_mum1': 2,
     'my_num2': 3,
     'my_str': 'you are breathtaking!',
     'pprint': <module 'pprint' from 'C:\\Users\\User\\miniconda3\\lib\\pprint.py'>,
     'say_hello': <function say_hello at 0x000001C557C01310>,
     'summa': <function summa at 0x000001C557EB63A0>}
 '''

# Обратите внимание, что инструкция import добавляет имя в пространство имен

import math

pprint.pprint(dir(math))  # вызовем пространство имен
''' вывод 
    ['__doc__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'acos',
     'acosh',
     ...
     'tau',
     'trunc']
'''

# в списке выше неясно, что именно такое перечисленно - переменная, функция и пр.
# поэтому можно зажать CTRL, навести на название модуля и перейти
# в него (откроется описание отдельным файлом)

print(math.pi)  # --> 3.141592653589793 аналогично можем обращаться к остальным переменным модуля
print(math.factorial(10))  # --> 3628800 обращение к встроенным в модуль функциям

# ---------------------- вариант импорта с псевдонимом

import math as m
print(m.pi)  # --> 3.141592653589793 обращение через псевдоним

# ---------------------- вариант импорта части модуля
# ВАЖНО! при импорте не допустить повтора имен, иначе последняя упомянутая затирает предыдущую

from math import e, pi, factorial  # имена подключаться в область видимости напрямую, без указания имени модуля
print(e, pi)  # 2.718281828459045 3.141592653589793 обращаться тоже можно напрямую, без указания модуля
print(factorial(3))

from math import factorial as fuct
print(fuct(3))

# ---------------------- вариант импорта всех имен модуля
from math import *  # плохой вариант, никогда не знаешь что подгрузил и что перезатрется

''' Стандарт: при импорте модуля каждый отдельно, при импорте имен из модуля через запятую одной строкой'''
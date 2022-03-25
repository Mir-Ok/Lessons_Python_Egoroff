''' По сути, декоратор - это то же самое замыкание, но во внешнюю функцию подается не переменная, а другая функция, см. конец предыдущего урока про замыкания '''

def decorator(func):

    def inner():
        
        print('start decorator ...')
        func()  # вызываем функцию, что подавали в аргументы
        print('finish decorator ...')

    return inner  # возвращаем без вызова

def say():
    print('hello world')

''' Вызовем внешнюю функцию, подадим ей в аргумент другую функцию и сохраним это в переменную. Переменная стала функцией '''

d = decorator(say)
print(d)  # --> При вызове мы видим, что здесь хранится функция inner(), вложенная в decorator() 

d() # --> при вызове отрабатывает inner(), которая сначала печатает start decorator, потом вызывает переданную функцию say()? которая в свою очередь
    # выводи на печать hello world, потом снова возвращается в inner() и выводит finish decorator:

''' вывод 

    start decorator  
    hello world
    finish decorator  
'''

''' Все описанные выше в полной мере совпадает с материалом урока по замыканиям. А что если мы хотим расширить функциональность функции say() 
    за счет возможностей функции decorator()?  
    
    Декоратор - это функция, которая принимает функцию и возвращает функцию, тем самый расширяя функционал принимаемой функции
    
    Важно! Называтся декоратор должен так же, как функция, которую мы хотим расширить, в данном случае say() 
    Мы ее словно подменяем/обновляем , но при записи подмены подаем в нее старую версию функции    

say = decorator(say)  # Теперь по имени say() мы храним функцию inner(), в которую передана функция say()
say()

''' вывод 
    start decorator ...
    hello world
    finish decorator ...
'''
print(say)  # <function decorator.<locals>.inner at 0x000001D407DD14C0>

# Если мы хотим добавить аргументы функциям, то надо добавить их и в замыкании

def decorator(func):

    def inner(n, m):  # для улучшения кода сразу пишем (*args, **kwargs)
        print('start decorator ...')
        func(n, m)   # для улучшения кода сразу пишем (*args, **kwargs)
        print('finish decorator ...')

    return inner

def say(name, surname):
    print('hello', name, surname)

say = decorator(say)
say('Vasya', 'Ivanov')
''' вывод 
    start decorator ...
    hello Vasya Ivanov
    finish decorator ...
'''

# ------------------------------------ еще пример, на одну функцию один декоратор

def header(func):

    def inner(*args, **kwargs):  # для улучшения кода сразу пишем (*args, **kwargs)
        print('<h1>')
        func(*args, **kwargs)   # для улучшения кода сразу пишем (*args, **kwargs)
        print('</h1>')

    return inner

def say(name, surname, age):
    print('hello', name, surname, age)

say = header(say)
say('Vasya', 'Ivanov', 30)
''' вывод 
    <h1>
        hello Vasya Ivanov 30
    </h1>
'''

# ------------------------------------ еще пример, на одну функцию несколько декораторов

def table(func):

    def inner(*args, **kwargs):  # для улучшения кода сразу пишем (*args, **kwargs)
        print('<table>')
        func(*args, **kwargs)   # для улучшения кода сразу пишем (*args, **kwargs)
        print('</table>')

    return inner

def say(name, surname, age):
    print('hello', name, surname, age)

say = table(header(say))
say('Vasya', 'Ivanov', 30)
''' вывод 
    <table>
        <h1>
            hello Vasya Ivanov 30
        </h1>
    </table>
'''

# Как получилось? Сначала вызвали header(), после table(). То есть результат работы первой
# функции попадает во вторую, поэтому обертка тегами идет последовательно


# ------------------------------------
''' Важный нюанс - оформиление записи декорирования. 
    say = table(header(say)) - так не пишут, декораторы навешивают при помощи тега @ перед функцией '''

@header  # аналогично say = header(say)
def say(name, surname, age):
    print('hello', name, surname, age)

say('Vasya', 'Ivanov', 30)
''' вывод 
    <h1>
        hello Vasya Ivanov 30
    </h1>
'''

@header
@table  # аналогично say = table(header(say)) первая ближе к say
def say(name, surname, age):
    print('hello', name, surname, age)

say('Vasya', 'Ivanov', 30)
''' вывод 
    <h1>
        <table>
            hello Vasya Ivanov 30
        </table>
    </h1>
'''

# --------------------------------------------------------
# Проблема - как не потерять имя задекорированной функции?
''' При создании функции она получает системное имя '''

def say():
    print('hello world')
print(say)  # --> <function __main__.say()>
say.__name__  # --> 'say'

''' После декорирования ее название меняется, она ссылается на замыкание '''
say = table(say)
print(say)  # --> <function __main__.table.<locals>.inner(*args, **kwargs)>
say.__name__  # --> 'inner'


''' Аналогичная проблема создается при вызове документации 
    Для примера определим функцию со всей документацией '''

def sqr(x):
     """
     Функция возводит в квадрат х
     :param x:
     :return:
     """
     print(x**2)

sqr.__name__  # --> 'sqr'
sqr.__doc__  # --> '\n Функция возводит в квадрат х\n     :param x:\n      :return:'
help(sqr)  # --> вызов справки в удобной форме
''' вывод 
    sqr(x)
        Функция возводит в квадрат х
        :param x:
        :return:
        '''

''' После декорирования мы потеряем справку, так как у функции inner документации нет '''
sqr = table(sqr)
sqr.__doc__  # --> пусто

# Вариант решения ВРУЧНУЮ, перед возвратом inner

def table(func):

    def inner(*args, **kwargs):  # для улучшения кода сразу пишем (*args, **kwargs)
        print('<table>')
        func(*args, **kwargs)   # для улучшения кода сразу пишем (*args, **kwargs)
        print('</table>')

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner

# Вариант декоратора wraps.
# Импортируем библиотеку, аргументом во wraps подаем функцию, которую декорируем

from functools import wraps

def table(func):

    @wraps(func)
    def inner(*args, **kwargs):  # для улучшения кода сразу пишем (*args, **kwargs)
        print('<table>')
        func(*args, **kwargs)   # для улучшения кода сразу пишем (*args, **kwargs)
        print('</table>')

    return inner

def main_func():  # --- создаем главную функцию
    def inner_func():  # --- создаем вложенную функцию
        print('hello, friens')
    inner_func()  # --- вызываем вложенную функцию внутри главной

main_func()
a = main_func()
print(a)  # --> None потому что в функции нет return, она ничего не возвращает

''' изменим ситуацию, создадим возврат ''' 

def main_func():  # --- создаем главную функцию
    def inner_func():  # --- создаем вложенную функцию
        print('hello, friens')
    return inner_func  # --- возвращаем внутреннюю функцию при вызове главной, НЕ вызываем, нет ()

''' в результате помещения главной
    функции в переменную, при вызове этой переменной мы будем получать ответ (см. ниже)
    он говорит нам, что пременная ссылается на вложенную функцию, находящуюся в главной
    
    по сути, переменная b является самой функцией, ее можно вызвать  '''

main_func()
b = main_func()
print(b)  # --> <function main_func.<locals>.inner_func at 0x000001E83C481310>

b() # --> hello, friens пример вызова переменной, которая стала функцией

''' Таким образом, мы создали замыкание, то есть возвращение вложеннной функции через обращение к главной без ее вызова 
    
    Чтобы завершить создание замыкания добавим переменную в главную функцию, для вложенной функции она будет глобальной
        
    ВАЖНО! после отработки функции, переменная не будет удалена, хотя после стандартного вызова локальной 
    функции все переменные уходят '''

def main_func():  # --- создаем главную функцию
    name = 'Ivan'  # --- объявляем нелокальную переменную
    def inner_func():  # --- создаем вложенную функцию
        print('hello, friens', name)
    return inner_func  # --- возвращаем внутреннюю функцию при вызове главной

''' Теперь мы можем вызывать функцию, передавать ей параметр и помещать значение в переменную
    немного напоминает работу с экземплярами класса
    '''

def main_func(value):  # --- создаем главную функцию
    name = value  # --- объявляем нелокальную переменную
    def inner_func():  # --- создаем вложенную функцию
        print('hello, friens', name)
    return inner_func  # --- возвращаем внутреннюю функцию при вызове главной

''' При каждом вызове главной функции и помещении ее в переменную создается свое пространство имен и области видимости,
сильно напоминает создание экземпляров класса '''

d = main_func('Petr')  # --> hello, friens Petr
d()
e = main_func('Anya')  # --> hello, friens Anya
e()
f = main_func('Fetr')  # --> hello, friens Fetr
f()

''' Рассмотрим пример 1

def adder(value_a):
    def inner(value_i):
        return value_a + value_i
    return inner  # --- для создания замыкания мы должны вернуть вложенную функцию, но без вызова

# Вызовем главную функцию и поместим ее в переменную. Т.к. главная функция вернула вложенную, переменная сама стала функцией, которая может принять аргумент

a2 = adder(2)
print(a2(5))  # --> 7

''' Что произошло выше?
    Создалась область видимости главной функции adder(), она же scope, в которой мы в value_a поместили 2 
    Далее мы вызвали переменную, в которой лежит главная функция и получили возможность передать переменную во вложенную функцию, и поместили 5 в value_i 
    Вложенная функция сработала и просуммировала, как и заложено выше.
    '''
    
a5 = adder(5)  # --> положили в value_a 5
print(a5(10))  # --> 15 положили в value_i 10 и суммировали


# Пример 2, счетчик

def counter():
    count = 0  # свободная переменная
    def inner():
        nonlocal count  # указываем что ссылаемся на переменную выше, она нелокальная для вложенной функции
        count += 1  # изменяем переменную в другой области видимости
        return count

    return inner  # вернем саму же функцию без () чтобы создать замыкание

q = counter()
print(q())  # --> 1
print(q())  # --> 2
print(q())  # --> 3
print(q())  # --> 4

# каждый вызов показывает, сколько раз вызывалась функция

r = counter()
print(r())  # --> 1
print(r())  # --> 2

''' каждый раз, когда мы будем вызывать функцию и помещать ее в новую переменную,
    будет создаваться своя область видимости, которая будет хранить свое
    значение переменной count
    
    Снова очень похоже на работу экземпляров класса в ООП
    
    Резюме - чтобы создать замыкание:
        1. Создаем внешнюю функцию, в которую помещаем вложенную
        2. Создаем return вложенной функции при вызове внешней, но без ()
        3. Добавляем переменную во внешнюю функцию, доступ к которой имеет сложенная
    
Внутренняя функция не будет выполняться автоматически без явного ее вызова
Благодаря return без () вложенная функция не вызывается, а передается из "функции-обертки" в "переменную", в которую поместили вызов внешней функции 
После чего переменная "становится" (имя ссылается на) вложенной функцией 

() - оператор вызова, сообщает интерпретатору, что функция вызывается, то есть выполняются описанные в ее теле инструкции.

В данном случае а() равносильно func() 

'''

# ------------------------------------------------------------------------------------------
# Часть 2

''' Пример 1. 
    Создаем функцию, которая с каждым вызовом принимает переменную, помещает ее в список
    и находит среднее арифметическое списка '''
    
def average_numbers():
    
    numbers = []  # его мы ниже не делаем nonlocal списки являются изменяемыми объектами. И то что, мы с ними делаем в функции будет видно и вне функции
    
    def inner(number):
        numbers.append(number)
        print(numbers)
        return sum(numbers) / len(numbers)

    return inner

d1 = average_numbers()  # d1 становится вложенной функцией и начинает принимать аргументы
print(d1(5))  # первое пополнение пустого списка и расчет средне-арифметического
print(d1(6))  # второе пополнение списка и расчет средне-арифметического
print(d1(7))  # третье пополнение списка и расчет средне-арифметического

'''вывод 
   [5]
   5.0
   [5, 6]
   5.5
   [5, 6, 7]
   6.0        
   '''

''' Можем несколько изменить функцию, и сразу считать суммы и количество, без изменяемого объекта [] 
    
    Заведем во внешней функции две свободные переменные, а во внутренней 
    дадим указание брать переменные из более сташей области видимости  через nonlocal 
    
    Это нужно, потому что мы хотим не просто задействовать переменные,  а именно изменять их  '''
    

def average_numbers():
    summa = 0
    count = 0

    def inner(number):
        nonlocal summa
        nonlocal count
        summa += number
        count += 1
        return summa / count

    return inner

d3 = average_numbers()
print(d3(10))  # --> 10
print(d3(20))  # --> 15
print(d3(30))  # --> 20


''' Пример 2. 
    Функция-таймер, которая будет засекать время с первого вызова функции '''

from datetime import datetime

def timer():
    
    start = datetime.now()  # запоминаем время первого вызова
    def inner():
        return datetime.now() - start  # получаем время текущего вызова и вычитаем из него время первого
    return inner

r = timer()  # в момент вызова в переменную вернется вложенная функция
             # и инициализируется переменная start, вней запишется время первого вызова
             
print(r())  # --> 0:00:00 так как запускаю все одновременно разницы нет

''' Немного улучшим результат, чтобы получать разницу во времени в секундах '''

from time import perf_counter

def timer():
    start = perf_counter()  # запоминаем время первого вызова
    def inner():
        return perf_counter() - start  # получаем время текущего вызова и вычитаем из него время первого
    return inner

r1 = timer()
print(r1())  # --> 5.999999999999062e-07

''' Пример 3
    Подача функции в качестве аргумента '''

def add(a,b):
    return a+b

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count +=1
        print(f'функция {func.__name__} вызывалась {count} раз')  # func.__name__ вернет название функции
        return func(*args, **kwargs)

    return inner

q = counter(add)
print(q(10, 20))  # функция add вызывалась 1 раз 30
print(q(15, 20))  # функция add вызывалась 2 раз 35
print(q(35, 20))  # функция add вызывалась 3 раз 55

''' Как так получилось?
    Мы вызываем counter() и передаем ей параметром другую функцию add()
    В переменную func сохранится название этой функции 
    
    В переменную q сохранится замыкание, функция inner()
    
    При вызове q(), ее параметры запомнятся в параметре *args
    
    Увеличиваем счетчик, выводим на печать отчет о количестве вызовов
    
    Вызываем саму функцию, так как inner() должна вернуть результат работы func (и поэтоиу она сама ее вызовет), 
    а это у нас изначально поданная в counter() функция add() '''

# Проверим работу счетчика на поримере другой функции

def mult(a, b, c):
    return a*b*c

m = counter(mult)
print(m(1, 20, 6))  # функция mult вызывалась 1 раз 120

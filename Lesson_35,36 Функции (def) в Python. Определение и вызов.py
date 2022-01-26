'''
Функция - многократно используемый фрагмент программы.
При помощи функции можно объединить несколько инструкций в один блок, присвоить ему имя и затем, обращаясь к блоку по имени,
выполнить инструкции внутри него в любом месте программы нужное количество раз.

Задание имени и содержание - определение функции. Всегда перед вызовом.

Внутри функции возможно использование циклов, условных операторов.

В отладчике, чтобы попасть внутрь функции, нажимаем вертикальную стрелку, направленную вниз. Step Into

При создании функции  мы можем задать ее аргументы. Бывают позиционные и именованные

Если переопределеить функцию ниже по телу кода - ее содержание перезапишется.
'''

# _1 функция без аргумента

def sayHello(): # определение функции
    print('hello', end = ' ')
    print('world', end = ' ')
    print('and you')

sayHello() # вызов функции
''' вывод: hello world and you '''

# _2 функция с одним аргументом. При вызове обязательно надо подать РОВНО один аргумент

def square(x):
    print('Квадрат числа', x, 'равен', x**2)

square(5)
''' вывод: Квадрат числа 5 равен 25 '''
# square()
''' вывод: TypeError: square() missing 1 required positional argument: x '''
# square(2,3)
''' вывод: TypeError: square() takes 1 positional argument but 2 were given '''

# _3 функция с двумя аргументами
def multiply(a,b):
    print(a*b)

multiply(3,8)
''' вывод: 24 '''

# --------------------------------------------------------------
# Когда могут потребоваться функции?

# _1 пример, уменьшение кол-ва кода

import turtle  # -- позволяет рисовать на экране

turtle.speed(1)  # -- задаем скорость движения
turtle.forward(100)  # -- рисуем квадрат
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.goto(150,150)  # -- перемещение в другую точку с указанными координатами

turtle.forward(100)  # -- рисуем квадрат
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

def drawSquare():
    turtle.forward(100)  # -- рисуем квадрат
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

turtle.speed(1)  # -- задаем скорость движения
drawSquare()
turtle.goto(150,150)  # -- перемещение в другую точку с указанными координатами
drawSquare()

# _2  декомпозиция большой задачи на маленькие кусочки и их связь между собой
# оптимизировать код, убираем дубли инструкций, упаковав их в функцию. Было 19 строк, стало 13

def move():
    turtle.forward(100)
    turtle.left(90)

def drawSquare():
    for i in range(4):
        move()

drawSquare()

# дополним код аргументом, чтобы добавить вариативности

def move(a):
    turtle.forward(a)
    turtle.left(90)

def drawSquare(a):
    for i in range(4):
        move(a)

drawSquare(5)
turtle.goto(150,150)  # -- перемещение в другую точку с указанными координатами
drawSquare(20)

# _3  декомпозиция, улучшение функционала

def move(a):  # -- кусочек траектории
    turtle.forward(a)
    turtle.left(90)

def drawSquareColor(a, color):  # -- описание движения, в аргументах сторона квардрата и его цвет
    turtle.color(color)  # -- передаем цвет
    turtle.begin_fill()  # -- начало закрашивания
    drawSquare(a)  # -- вместо двух строк ниже
    # for i in range(4):  # -- отрисовка контура
    #    move(a)
    turtle.end_fill()  # -- окончание закрашивания

drawSquareColor(50, 'red')
turtle.goto(200,250)  # -- перемещение в другую точку с указанными координатами
drawSquareColor(100, 'blue')
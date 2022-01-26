
# Функция input() - которая считывает введенное пользователем в консоль значение и сохраняет его в программе

a = input()       # запросит ввод
print(type(a))    # выведет в консоль его тип, базово всегда строка

b = int(input())         # ввод целого числа
c = float(input())       # ввод вещественного числа

# При запросе нескольких чисел подряд, каждое надо подавать отдельно, на своей строке и нажимая Enter.
# Если ввести их строкой через пробел, Питон выдаст ошибку, возьмет только первое число, а дальше заругается на пробел.
# Правильный способ ввода через функцию map()

a, b, c = map(int, input().split())

# -----------------------------------------------------------

# Функция print() - которая считывает введенное пользователем в консоль значение и сохраняет его в программе

# По умолчанию, элементы при выводе разделены пробелом. Мы можем его заменить при помощи атрибута sep = ''

print(1, 2, 3)            # --> 1 2 3
print(1, 2, 3, sep='_')   # --> 1_2_3 изменили сепаратор между цифрами
print(1, 2, 3, sep='')    # --> 123

# По умолчанию, в конце строки стоит перенос \n. Мы можем его заменить при помощи атрибута end = ''

print(1, 2, 3, end = '')
print(1, 2, 3, sep='_')   # --> 1 2 3 1_2_3 все в одну строку, потому что перехода на новую строку не было

# Способы вывода переменных в тексте

rub = 10
kop = 99

print('У меня есть ', rub, 'рублей и ', kop, 'копеек')        # -->  'У меня есть 10 рублей и 99 копеек'
print('У меня есть %s рублей и  %s копеек' % (rub, kop))      # -->  'У меня есть 10 рублей и 99 копеек'

print('{0}, {1}, {2}'.format('a', 'b', 'c'))     # -->  'a, b, c'
print('{}, {}, {}'.format('a', 'b', 'c'))        # -->  'a, b, c'
print('{2}, {1}, {0}'.format('a', 'b', 'c'))     # -->  'c, b, a'
print('{2}, {1}, {0}'.format(*'abc'))            # -->  'c, b, a'
print('{0}{1}{0}'.format('abra', 'cad'))         # -->  'abracadabra'

print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
      # -->  'Coordinates: 37.24N, -115.81W'

# Подробнее про метод .format() https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html

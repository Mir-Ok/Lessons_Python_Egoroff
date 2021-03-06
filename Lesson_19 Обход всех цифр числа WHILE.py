x = 2587  # --- задаем переменную
x1 = x
kol = 0  # ---- счетчик количества
kol_ch = 0  # - счетчик четных
sum = 0  # ---- счетчик суммы
pr = 1  # ----- счетчик произведения
max = 0
min = 9

while x > 0:  # ------------ проверка условия
    last = x % 10  # ------- выводим последнее число, взяв остаток от деления на 10
    kol += 1  # ------------ увеличиваем счетчик
    if last % 2 == 0:  # --- проверка на четность
        kol_ch += 1  # ----- увеличение счетчика, если да
    sum += last  # --------- добавление цифры к общей сумме
    pr *= last
    if last > max:
        max = last
    if last < min:
        min = last
    x = x // 10  # --------- убираем из переменной последнюю цифру

print('Число: ', x1)
print('Всего цифр: ', kol)
print('Всего четных цифр: ', kol_ch)
print('Всего сумма цифр: ', sum)
print('Всего произведение цифр: ', pr)
print('Минимальная цифра: ', min)
print('Максимальная цифра: ', max)

''' вывод
Число:  2587
Всего цифр:  4
Всего четных цифр:  2
Всего сумма цифр:  22
Всего произведение цифр:  560
Минимальная цифра:  2
Максимальная цифра:  8
'''

# Перевод числа в другие системы счисления.
# Если мы используем x % 10, мы используем десятеричную систему счисления.
# ВАЖНО! В коде вывод идет справа налево

'''
Попробуем разложить числа  в двоичной записи. 
Для этого нам потребуются степени числа 2, такие как 16,8,4,2,1. 
Степени выше тоже используются для более крупных чисел.

Разложим на слагаемые 14. 14 = 16*0 + 8*1 + 4*1 + 2*1 + 1*0.
Поэтому 14 в двоичной системе это 1110.
Разложим на слагаемые 16. 16 = 16*1 + 8*0 + 4*0 + 2*0 + 1*0
Поэтому 16 в двоичной системе это 10000
'''

x = 14
while x > 0:
    last = x % 2
    print(last)
    x = x // 2
''' вывод 
0
1
1
1
'''

'''
Попробуем разложить числа  в пятеричной записи. 
Для этого нам потребуются степени числа 5, такие как 25,5,1. 
Степени выше тоже используются для более крупных чисел.

Разложим на слагаемые 43. 43 = 25*1 + 5*3 + 1*3.
Поэтому 43 в двоичной системе это 133.
'''

x = 43
while x > 0:
    last = x % 5
    print(last)
    x = x // 5
''' вывод 
3
3
1
'''
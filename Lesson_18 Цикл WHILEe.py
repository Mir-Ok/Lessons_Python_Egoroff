# Инструкция для реализации циклов с неизвестным количеством повторений

'''
С помощью него можно:
- обходить числа пока они меньше (больше) определенного значения
- заставлять вводить пользователя до тех пор пока он не введет нужное значение
- обрабатывать списки и строки

Общий вид:

while условие:
    инструкции в цикле 1
    инструкции в цикле 2
    ...
    инструкции в цикле N
инструкции вне цикла

Пока условие верно, инструкции (на одном табе, 4 пробела)
выполняются. Как только нет - выполняется следующее за циклом выражение
'''

# работа с цифрами

i = 15 # -------- исходное значение переменной
while i > 10: # - проверка условия
    print(i) # -- выполнение
    i = i - 1 # - увеличение значения переменной
''' вывод
15
14
13
12
11
'''

# работа с текстами

guess = input() # --------------------------------- запрос на ввод текста
password = 'qwerty' # ----------------------------- заданное значение пароля
count = 0 # --------------------------------------- счетчик попыток
while guess != password: # ------------------------ проверка условия
    count += 1 # ---------------------------------- увеличение счетчика на шаг
    print('Пароль неверный!') # ------------------- реакция при выполнении условия
    guess = input() # ----------------------------- новый запрос на ввод текста
print('Пароль верный') # -------------------------- вывод после завершения цикла
print('Вы использовали', count + 1, 'попыток') # -- вывод кол-ва неудачных попыток +1 удачная

''' вывод
укарр
Пароль неверный!
арарра
Пароль неверный!
qwerty
Пароль верный
Вы использовали 3 попыток
'''

# работа со списками

# метод .remove выдает ошибку, если элемента нет. В цикле с проверкой условия ошибок не будет,
# просто пропустит. Например, если б задали удаление цифры 5 (которой нет изначально)

a = [1,2,3] * 3
print(a)
while 3 in a:
    a.remove(3)
    print(a)
''' вывод
[1, 2, 3, 1, 2, 3, 1, 2, 3]
[1, 2, 1, 2, 3, 1, 2, 3]
[1, 2, 1, 2, 1, 2, 3]
[1, 2, 1, 2, 1, 2]
'''

# работа с символами

s = 'hHf4"-5g' # -------------------- задаем переменную
while len(s) > 0: # --------------- пока ее длина больше 0
    bukva = s[0] # ---------------- берем первый символ переменной
    if 'a' <= bukva <='z': # ------ проверяем на ...
        print(bukva, 'small') # ---
    elif 'A' <= bukva <='Z': # ----
        print(bukva, 'big') # -----
    elif bukva.isdigit(): # -------
        print(bukva, 'digit') # ---
    else:
        print(bukva, 'znak')  # ---
    s = s[1:] # ------------------- удаляем из заданной переменной первый символ, уменьшая ее длину
''' вывод 
h small
H big
f small
4 digit
" znak
- znak
5 digit
g small
'''
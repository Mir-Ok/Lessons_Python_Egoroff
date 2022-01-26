# Способы создания текста

a = 'текст'
b = "текст"
c = '''hello
world
258'''

print(a)
print(b)
print(c)    # тройные кавычки дают возможность вводить многострочные текстовые переменные

# 1. Конкатенация - сцепление, сложение строк
print('abc' + 'def')           # --> 'abcdef' плюсовать можно только строковые переменные
print('a' * 5)                 # --> 'aaaaa' умножаем только на целые числа

# 2. вычисление длины строки
print(len('ahcyrjfhfh'))       # --> 10 считает все, включая пропуски и знаки препинания

# 3. Проверка наличия символа в строке
f = 'ahcyrjfhfh'
print('c' in f)                # --> True
print('yc' in f)               # --> False порядок важен

# 4. Сравнение строк
print('aaa' == 'aaa')          # --> True совпадают, когда равны символы, длина и регистры
print('aaa' == 'AAA')          # --> False

print('abc' > 'r')             # --> False т.к. первые символы находятся на разном расстоянии от начала алфавита,
                               #           не по длине. Сравниваются символьные обозначения из ascii code table,
                               #           ord('a') равно 97, ord('r') = 114

print('ABCD' > 'r')            # --> False  заглавные буквы всегда меньше строчных

print('abcd' > 'abc')          # --> True  все совпадающие равны, на четвертом месте в одной из строк пустота

print('aaa' > 'aaa ')          # --> False
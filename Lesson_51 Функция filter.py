'''
Очен похожа на map, первым аргументов принимает функцию, вторым - итерабельную последовательность.
И результатом ее работы будет объект filter, итератор, и в него войдут только те элементы,
для которых функция вернет значение TRUE (функции, которые возвращают не булевы значения для этой функции не подойдут).

'''

def f(x):
    return x > 10  # сразу вернет True/False, подставляя значения из списка
    # if x > 10:  длинная запись новичков
    #     return True
    # else:
    #    return False

a = [14, 0, 5, 79, 645, 7952, 18, 0, 192, 471]
b = filter(f, a)
print(b)  # --> <filter object at 0x0000022215487100>

d = list(filter(f, a))  # надо преобразовать к коллекции, фунцию подаем в аргумент без скобок
print(d)  # --> [14, 79, 645, 7952, 18, 192, 471]

e = [i for i in a if i % 10 == 2]  # аналогичная фильтрация списка через генератор списков
print(e)  # --> [7952, 192]

''' 
есть возможность передавать не только самописные функции, но и встроенные,
но при условии, что функция вернет булеов значение
'''

a = [14, 0, 5, 79, '', 'hhh', 645, 7952, 18, 0, 192, 471]
b = list(filter(bool, a))  # функция bool вернет истину для всех чисел, кроме 0 b для всех строк, кроме пустоты
print(b)  # --> [14, 5, 79, 'hhh', 645, 7952, 18, 192, 471] ноля и пустоты в списке нет

# вместо bool можно поставить None, это не изменит ситуацию

''' 
есть возможность подавать анонимные функции lambda
'''

a = ['12345', '123','1234','123456','1234567']
b = list(filter(lambda x: len(x)>4, a))
print(b)  # --> ['12345', '123456', '1234567']

''' 
есть возможность подавать методы, которые возвращают true / false
'''

a = 'авлоFrвша4545аа'
b = list(filter(str.isdigit, a))
print(b)  # --> ['4', '5', '4', '5']

a = 'авлоDEGвша4545аа'
b = list(filter(str.isalpha, a))
print(b)  # --> ['а', 'в', 'л', 'о', 'в', 'ш', 'а', 'а', 'а']

a = 'авлоDEGвша4545аа'
b = list(filter(str.isupper, a))
print(b)  # --> ['D', 'E', 'G']

''' 
фильтрация словаря
'''
d = {
    'moscow': 800,
    'boston': 750,
    'LA': 400,
    'SF': 900,
    'Chicago': 650,
    'SP': 600,
}

b = list(filter(lambda x: d[x] > 600, d))  # в х будут сохраняться именно ключи
print(b)  # --> ['moscow', 'boston', 'SF', 'Chicago']